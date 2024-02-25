from fabric.api import task


@task
def hello(c):
    print("Hello from Fabric!")
