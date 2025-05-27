import subprocess
import json
from pathlib import Path

@click.command()
@click.argument('target', type=click.Path(exists=True))
@click.option('--format', type=click.Choice(['text', 'json']), default='text')
@click.option('--focus', type=click.Choice(['bugs', 'style', 'all']), default='all')
def review(target, format, focus):
    """Review code using Claude Code SDK."""
    content = read_file_content(target)
    result = call_claude_code(content, focus)

        # Parse and format output
    if format == 'json':
        click.echo(result)
    else:
        # Parse JSON and extract just the result text
        data = json.loads(result)
        click.echo(data.get('result', 'No result found'))

def read_file_content(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def call_claude_code(content, focus):
    # Create prompt based on focus
    if focus == "bugs":
        prompt = f"Review this code for bugs and errors:\n\n{content}"
    if focus == "style":
        prompt = f"Review this code for problems with the style:\n\n{content}"
    else:
        prompt = f"Review this code for bugs and errors as well as problems with the style:\n\n{content}"

    # Call Claude Code CLI
    result = subprocess.run(['claude', '-p', prompt, '--output-format', 'json'], 
                          capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    review()
