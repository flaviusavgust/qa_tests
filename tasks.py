from invoke import task

@task
def test(c, env='staging', lang='en', app='android', device='emulator'):
    """
    update local storage
    Enable and modify this to add local storage
    """
    # os.system("adb push $(pwd)/data/<your_app_prefs_file>.xml /data/data/<packageName>/shared_prefs")
    c.run(f'python3 -m pytest src/spec/{app}/*.py --app={app} --device={device}')