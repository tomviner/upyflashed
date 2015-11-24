MICROBIT = 'MICROBIT'

def read_dbus():
    """
    Based on http://stackoverflow.com/a/5081937/15890


    extra_requires={
        'linux': [
            'dbus-python',
        ],
    },
    """
    try:
        import dbus
    except ImportError:
        return

    bus = dbus.SystemBus()
    ud_manager_obj = bus.get_object("org.freedesktop.UDisks", "/org/freedesktop/UDisks")
    ud_manager = dbus.Interface(ud_manager_obj, 'org.freedesktop.UDisks')

    for dev in ud_manager.EnumerateDevices():
        device_obj = bus.get_object("org.freedesktop.UDisks", dev)
        device_props = dbus.Interface(device_obj, dbus.PROPERTIES_IFACE)
        mount_paths = device_props.Get('org.freedesktop.UDisks.Device', "DeviceMountPaths")
        for mount_path in mount_paths:
            if MICROBIT in mount_path:
                return str(mount_path)
