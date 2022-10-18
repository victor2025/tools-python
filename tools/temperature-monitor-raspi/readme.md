# Temperature Monitor for Raspi

### Environment
- raspbian
- python3.7

### Install
- Run `install.sh` with root privilege

### Usage
- Install program.
- Complete configure files in `/etc/temper-monitor`, here is the introduction of configure files of [email_sender](src/email_sender/readme.md).
- Start service with `systemd`:
    ```bash
    sudo service temper-monitor start
    sudo systemctl enable temper-monitor
    ```

### Source Code
- Change warn mode by creating different `temperMonitor` in `temperMonitorMain.py`.
- Run `tempMonitorMain.py` to start monitor.
- Log module: [log_helper](src/log_helper/readme.md).
- Email module: [email_sender](src/email_sender/readme.md).

