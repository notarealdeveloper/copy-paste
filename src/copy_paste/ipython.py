# copy_paste using ipython line and cell magic

__all__ = [
    'install',
]

from IPython import get_ipython # necessary!

from IPython.core.magic import register_line_cell_magic

def install():
    @register_line_cell_magic
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
