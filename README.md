# Automation

A collection of Python + Linux automation scripts built while learning core concepts for infrastructure automation, monitoring, and operations - service health checks, log monitoring, and API health checks, each with proper error handling and logging.

## Scripts

### `service_monitor.py`
Checks if a given systemd service is active, and automatically restarts it if it's down. Uses `subprocess` to interact with `systemctl`, with structured logging throughout.

**Usage:**
```bash
python3 service_monitor.py <service_name>
```

### `log_watcher.py`
Scans a log file for occurrences of a given text pattern and raises an alert if the count exceeds a configurable threshold. Useful for basic security monitoring, e.g. detecting repeated failed SSH login attempts.

**Usage:**
```bash
python3 log_watcher.py <log_path> "<pattern>" --threshold 5
```

### `api_health_check.py`
Checks whether a given URL/API endpoint is healthy, with automatic retries and configurable delay between attempts.

**Usage:**
```bash
python3 api_health_check.py <url> --retries 3 --delay 3
```

## Concepts covered
- Linux fundamentals: filesystem hierarchy, permissions, processes, `systemctl`, cron
- Python scripting: `subprocess`, `argparse`, `logging`, error handling, retry logic
- Automation: unattended scheduled execution via cron
- Monitoring/observability basics: log parsing, threshold-based alerting
- Git: branching, merge conflict resolution, remote workflows

## Environment
Developed and tested on an Ubuntu Server VM (VirtualBox), accessed via SSH.
