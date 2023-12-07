# copy_paste using ipython line and cell magic

__all__ = [
    'install',
    'install_xc',
    'install_xv',
]


def install():
    install_xc()
    install_xv()

def install_xc():
    from IPython.core.magic import register_line_cell_magic
    return register_line_cell_magic(xc)

def install_xv():
    from IPython.core.magic import register_line_cell_magic
    return register_line_cell_magic(xv)

def xc(line, cell=None):
    import subprocess
    if cell is None:
        # called as %xc (line magic)
        data = line
    else:
        # called as %%xc (cell magic)
        data = re.sub('\n+$', '\n', cell)

    s = data.encode()

    p = subprocess.Popen(
        ['xclip', '-selection', 'p'],
        stdin = subprocess.PIPE,
    )
    p.communicate(s)

    p = subprocess.Popen(
        ['xclip', '-selection', 'c'],
        stdin = subprocess.PIPE,
    )
    p.communicate(s)


def xv(line, cell=None):
    import subprocess
    if cell is None:
        # called as %xc (line magic)
        data = line
    else:
        # called as %%xc (cell magic)
        data = re.sub('\n+$', '\n', cell)

    data = str(eval(data))

    s = data.encode()

    p = subprocess.Popen(
        ['xclip', '-selection', 'p'],
        stdin = subprocess.PIPE,
    )
    p.communicate(s)

    p = subprocess.Popen(
        ['xclip', '-selection', 'c'],
        stdin = subprocess.PIPE,
    )
    p.communicate(s)
