from subprocess import run


def exec_cmd(cmd: str, *args) -> bool:
    """
    This executes a system command and returns whether it was successful or not

    :param cmd: Command to execute
    :param args: Any arguments to command
    :return: Successful or not
    """

    # Result object of the command
    # If an error occurs, this will be the value used
    result = None

    try:
        # Run the command and capture output
        result = run([cmd] + list(args),
                     capture_output=True,
                     text=True,
                     shell=True)
    except:
        pass

    # If the command completely crashed then return false
    if result is None:
        return False

    # Otherwise return false if stderr contains error messages and/or the return code is not 0
    return (not str(result.stderr)) and (result.returncode == 0)
