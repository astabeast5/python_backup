import psutil
from flask import Flask, render_template, jsonify
import time
from collections import deque
import threading
import platform
import subprocess
import os
import json
import socket
from datetime import datetime

app = Flask(__name__)

# Store historical data (last 200 data points for better analytics)
historical_data = {
    'timestamps': deque(maxlen=200),
    'cpu_data': deque(maxlen=200),
    'mem_data': deque(maxlen=200),
    'disk_data': deque(maxlen=200),
    'network_sent': deque(maxlen=200),
    'network_recv': deque(maxlen=200),
    'cpu_temp': deque(maxlen=200),
    'gpu_usage': deque(maxlen=200),
    'battery_percent': deque(maxlen=200)
}

# Performance analytics
performance_stats = {
    'cpu_avg': 0,
    'mem_avg': 0,
    'peak_cpu': 0,
    'peak_mem': 0,
    'alerts_count': 0
}

@app.route("/")
def index():
    return render_template("ultimate_monitor.html")

@app.route("/enhanced")
def enhanced():
    return render_template("index_enhanced.html")

@app.route("/quantum")
def quantum():
    return render_template("revolutionary_monitor.html")

def get_wsl_info():
    """Get WSL-specific information"""
    try:
        if 'microsoft' in platform.uname().release.lower():
            wsl_version = subprocess.check_output(['wsl', '--version'], text=True, stderr=subprocess.DEVNULL)
            return {'is_wsl': True, 'version': wsl_version.strip()}
    except:
        pass
    return {'is_wsl': False}

def get_network_stats():
    """Get network statistics"""
    try:
        net_io = psutil.net_io_counters()
        return {
            'bytes_sent': net_io.bytes_sent,
            'bytes_recv': net_io.bytes_recv,
            'packets_sent': net_io.packets_sent,
            'packets_recv': net_io.packets_recv
        }
    except:
        return {'bytes_sent': 0, 'bytes_recv': 0, 'packets_sent': 0, 'packets_recv': 0}

def get_cpu_temperature():
    """Get CPU temperature if available"""
    try:
        temps = psutil.sensors_temperatures()
        if temps:
            for name, entries in temps.items():
                if entries:
                    return round(entries[0].current, 1)
    except:
        pass
    return None

def get_gpu_info():
    """Get GPU information if available"""
    try:
        # Try nvidia-smi for NVIDIA GPUs
        result = subprocess.run(['nvidia-smi', '--query-gpu=utilization.gpu,memory.used,memory.total,temperature.gpu', '--format=csv,noheader,nounits'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            data = result.stdout.strip().split(', ')
            return {
                'usage': float(data[0]),
                'memory_used': float(data[1]),
                'memory_total': float(data[2]),
                'temperature': float(data[3])
            }
    except:
        pass
    return None

def get_battery_info():
    """Get battery information if available"""
    try:
        battery = psutil.sensors_battery()
        if battery:
            return {
                'percent': round(battery.percent, 1),
                'plugged': battery.power_plugged,
                'time_left': battery.secsleft if battery.secsleft != psutil.POWER_TIME_UNLIMITED else None
            }
    except:
        pass
    return None

def get_system_services():
    """Get running system services count"""
    try:
        services = list(psutil.win_service_iter()) if platform.system() == 'Windows' else []
        running = sum(1 for s in services if s.status() == 'running')
        return {'total': len(services), 'running': running}
    except:
        return {'total': 0, 'running': 0}

def get_disk_io():
    """Get disk I/O statistics"""
    try:
        disk_io = psutil.disk_io_counters()
        return {
            'read_bytes': disk_io.read_bytes,
            'write_bytes': disk_io.write_bytes,
            'read_count': disk_io.read_count,
            'write_count': disk_io.write_count
        }
    except:
        return {'read_bytes': 0, 'write_bytes': 0, 'read_count': 0, 'write_count': 0}

def collect_system_data():
    """Background thread to collect real system data"""
    prev_net = get_network_stats()
    prev_disk = get_disk_io()
    
    while True:
        try:
            # Get real system metrics
            cpu_percent = psutil.cpu_percent(interval=2, percpu=False)
            memory = psutil.virtual_memory()
            
            # Disk usage
            try:
                disk = psutil.disk_usage('/')
            except:
                disk = psutil.disk_usage('C:\\')
            
            # Network stats
            curr_net = get_network_stats()
            net_sent_rate = max(0, (curr_net['bytes_sent'] - prev_net['bytes_sent']) / 1024 / 1024)  # MB/s
            net_recv_rate = max(0, (curr_net['bytes_recv'] - prev_net['bytes_recv']) / 1024 / 1024)  # MB/s
            prev_net = curr_net
            
            # Additional metrics
            cpu_temp = get_cpu_temperature()
            gpu_info = get_gpu_info()
            battery_info = get_battery_info()
            
            timestamp = time.strftime('%H:%M:%S')
            
            # Store in historical data
            historical_data['timestamps'].append(timestamp)
            historical_data['cpu_data'].append(round(cpu_percent, 1))
            historical_data['mem_data'].append(round(memory.percent, 1))
            historical_data['disk_data'].append(round(disk.percent, 1))
            historical_data['network_sent'].append(round(net_sent_rate, 2))
            historical_data['network_recv'].append(round(net_recv_rate, 2))
            historical_data['cpu_temp'].append(cpu_temp or 0)
            historical_data['gpu_usage'].append(gpu_info['usage'] if gpu_info else 0)
            historical_data['battery_percent'].append(battery_info['percent'] if battery_info else 100)
            
            # Update performance analytics
            if len(historical_data['cpu_data']) > 10:
                performance_stats['cpu_avg'] = sum(list(historical_data['cpu_data'])[-10:]) / 10
                performance_stats['mem_avg'] = sum(list(historical_data['mem_data'])[-10:]) / 10
                performance_stats['peak_cpu'] = max(historical_data['cpu_data'])
                performance_stats['peak_mem'] = max(historical_data['mem_data'])
            
            time.sleep(2)  # Faster updates for better responsiveness
        except Exception as e:
            print(f"Error collecting data: {e}")
            time.sleep(5)

@app.route("/api/stats")
def get_stats():
    try:
        # Get current real-time data
        cpu_percent = psutil.cpu_percent(interval=0.1)
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        try:
            disk = psutil.disk_usage('/')
        except:
            disk = psutil.disk_usage('C:\\')
        
        # System info
        boot_time = psutil.boot_time()
        uptime = time.time() - boot_time
        uptime_hours = int(uptime // 3600)
        uptime_minutes = int((uptime % 3600) // 60)
        
        # Network info
        net_stats = get_network_stats()
        
        # WSL info
        wsl_info = get_wsl_info()
        
        # CPU temperature
        cpu_temp = get_cpu_temperature()
        
        # Top processes with more details
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'status', 'create_time']):
            try:
                if proc.info['cpu_percent'] > 0:
                    proc.info['runtime'] = time.time() - proc.info['create_time']
                    processes.append(proc.info)
            except:
                pass
        processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:15]
        
        # System services
        services = get_system_services()
        
        # GPU and Battery info
        gpu_info = get_gpu_info()
        battery_info = get_battery_info()
        
        # Disk I/O
        disk_io = get_disk_io()
        
        # Network interfaces
        network_interfaces = []
        try:
            for interface, addrs in psutil.net_if_addrs().items():
                for addr in addrs:
                    if addr.family == socket.AF_INET:
                        network_interfaces.append({'name': interface, 'ip': addr.address})
        except:
            pass
        
        stats = {
            'cpu_percent': round(cpu_percent, 1),
            'cpu_temp': cpu_temp,
            'cpu_cores_logical': psutil.cpu_count(logical=True),
            'cpu_cores_physical': psutil.cpu_count(logical=False),
            'cpu_freq': psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
            'mem_percent': round(memory.percent, 1),
            'mem_used': round(memory.used / (1024**3), 2),
            'mem_total': round(memory.total / (1024**3), 2),
            'mem_available': round(memory.available / (1024**3), 2),
            'swap_percent': round(swap.percent, 1),
            'swap_used': round(swap.used / (1024**3), 2),
            'swap_total': round(swap.total / (1024**3), 2),
            'disk_percent': round(disk.percent, 1),
            'disk_used': round(disk.used / (1024**3), 2),
            'disk_total': round(disk.total / (1024**3), 2),
            'disk_io': {
                'read_gb': round(disk_io['read_bytes'] / (1024**3), 2),
                'write_gb': round(disk_io['write_bytes'] / (1024**3), 2),
                'read_count': disk_io['read_count'],
                'write_count': disk_io['write_count']
            },
            'network': {
                'bytes_sent': round(net_stats['bytes_sent'] / (1024**3), 2),
                'bytes_recv': round(net_stats['bytes_recv'] / (1024**3), 2),
                'packets_sent': net_stats['packets_sent'],
                'packets_recv': net_stats['packets_recv'],
                'interfaces': network_interfaces
            },
            'gpu': gpu_info,
            'battery': battery_info,
            'services': services,
            'timestamp': time.strftime('%H:%M:%S'),
            'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'uptime': f"{uptime_hours}h {uptime_minutes}m",
            'platform': {
                'system': platform.system(),
                'release': platform.release(),
                'version': platform.version(),
                'machine': platform.machine(),
                'processor': platform.processor()
            },
            'wsl_info': wsl_info,
            'processes': processes,
            'performance_stats': performance_stats,
            'history': {
                'timestamps': list(historical_data['timestamps']),
                'cpu_data': list(historical_data['cpu_data']),
                'mem_data': list(historical_data['mem_data']),
                'disk_data': list(historical_data['disk_data']),
                'network_sent': list(historical_data['network_sent']),
                'network_recv': list(historical_data['network_recv']),
                'cpu_temp': list(historical_data['cpu_temp']),
                'gpu_usage': list(historical_data['gpu_usage']),
                'battery_percent': list(historical_data['battery_percent'])
            }
        }
        
        # Enhanced alert conditions
        alerts = []
        if cpu_percent > 85:
            alerts.append({'type': 'critical', 'message': f"Critical CPU usage: {cpu_percent:.1f}%"})
        elif cpu_percent > 70:
            alerts.append({'type': 'warning', 'message': f"High CPU usage: {cpu_percent:.1f}%"})
            
        if memory.percent > 90:
            alerts.append({'type': 'critical', 'message': f"Critical memory usage: {memory.percent:.1f}%"})
        elif memory.percent > 75:
            alerts.append({'type': 'warning', 'message': f"High memory usage: {memory.percent:.1f}%"})
            
        if disk.percent > 95:
            alerts.append({'type': 'critical', 'message': f"Critical disk space: {disk.percent:.1f}% used"})
        elif disk.percent > 85:
            alerts.append({'type': 'warning', 'message': f"Low disk space: {disk.percent:.1f}% used"})
            
        if cpu_temp and cpu_temp > 85:
            alerts.append({'type': 'critical', 'message': f"Critical CPU temperature: {cpu_temp}°C"})
        elif cpu_temp and cpu_temp > 75:
            alerts.append({'type': 'warning', 'message': f"High CPU temperature: {cpu_temp}°C"})
            
        if gpu_info and gpu_info['temperature'] > 80:
            alerts.append({'type': 'warning', 'message': f"High GPU temperature: {gpu_info['temperature']}°C"})
            
        if battery_info and battery_info['percent'] < 15 and not battery_info['plugged']:
            alerts.append({'type': 'warning', 'message': f"Low battery: {battery_info['percent']}%"})
            
        performance_stats['alerts_count'] = len(alerts)
            
        stats['alerts'] = alerts
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/export')
def export_data():
    """Export system data for analysis"""
    try:
        export_data = {
            'timestamp': datetime.now().isoformat(),
            'system_info': {
                'platform': platform.system(),
                'cpu_count': psutil.cpu_count(),
                'memory_total': psutil.virtual_memory().total
            },
            'historical_data': dict(historical_data),
            'performance_stats': performance_stats
        }
        return jsonify(export_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'uptime': time.time() - psutil.boot_time()
    })

if __name__ == '__main__':
    print("🎆 Starting Ultimate System Monitor Pro...")
    print(f"🎆 Ultimate Dashboard: http://localhost:5001")
    print(f"🌌 Quantum Dashboard: http://localhost:5001/quantum")
    print(f"📊 Enhanced Dashboard: http://localhost:5001/enhanced")
    
    # Start background data collection thread
    data_thread = threading.Thread(target=collect_system_data, daemon=True)
    data_thread.start()
    
    app.run(debug=True, host='0.0.0.0', port=5001, threaded=True)
