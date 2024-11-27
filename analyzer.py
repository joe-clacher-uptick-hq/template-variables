import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, Set, List

class VariableContext:
    def __init__(self):
        self.files: Set[str] = set()
        self.filters: Set[str] = set()
        self.examples: List[Dict] = []
        self.loop_contexts: Dict[str, Set[str]] = defaultdict(set)
        self.default_values: Set[str] = set()
        self.nested_patterns: Dict[str, Set[str]] = defaultdict(set)

def clean_example_content(content: str) -> str:
    """Clean up the example content by:
    1. Converting HTML entities back to tags
    2. Converting **var** to proper formatting
    3. Escaping Django template tags
    4. Cleaning up code blocks
    """
    # Convert HTML entities back to tags
    content = content.replace('&lt;', '<').replace('&gt;', '>')
    
    # Convert **variable** to proper formatting
    content = re.sub(r'\*\*\{\{(.*?)\}\}\*\*', r'`{{\1}}`', content)
    
    # Clean up other bold markers that aren't variables
    content = re.sub(r'\*\*(.*?)\*\*', r'**\1**', content)
    
    # Escape Django template tags for Jekyll
    content = content.replace('{% ', '{%raw%}{% ').replace(' %}', ' %}{%endraw%}')
    content = content.replace('{{', '{%raw%}{{').replace('}}', '}}{%endraw%}')
    
    return content


class TemplateAnalyzer:
    CSS_STYLES = """
<style>
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

details.expandable-section {
    margin: 10px 0;
    padding: 5px;
    border-radius: 4px;
}

details.expandable-section summary {
    cursor: pointer;
    padding: 8px;
    margin: -5px;
    border-radius: 4px;
    list-style: none;
}

details.expandable-section summary::-webkit-details-marker {
    display: none;
}

details.expandable-section summary::before {
    content: "▶";
    display: inline-block;
    margin-right: 8px;
    transition: transform 0.2s;
}

details.expandable-section[open] > summary::before {
    transform: rotate(90deg);
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #f5f5f5;
}

code {
    background-color: #f5f5f5;
    padding: 2px 4px;
    border-radius: 3px;
    font-family: monospace;
}

.loop-info {
    display: inline-block;
    position: relative;
    color: #666;
    font-size: 0.9em;
    margin-left: 8px;
    cursor: help;
}

.loop-info::after {
    content: "ℹ️";
    margin-left: 4px;
}

.loop-info .tooltip {
    visibility: hidden;
    position: absolute;
    z-index: 1;
    bottom: 125%;
    left: 50%;
    transform: translateX(-50%);
    width: 300px;
    background-color: #333;
    color: white;
    text-align: center;
    padding: 8px;
    border-radius: 6px;
    opacity: 0;
    transition: opacity 0.3s;
}

.loop-info:hover .tooltip {
    visibility: visible;
    opacity: 1;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #f5f5f5;
}

pre {
    background-color: #f8f8f8;
    padding: 15px;
    border-radius: 6px;
    overflow-x: auto;
    margin: 15px 0;
}

code {
    font-family: monospace;
    font-size: 14px;
    line-height: 1.5;
}

pre code {
    font-family: monospace;
    font-size: 14px;
    line-height: 1.5;
    white-space: pre-wrap;
    word-wrap: break-word;
    color: #333;
}

code strong {
    background-color: #fff3b8;
    padding: 2px 4px;
    border-radius: 3px;
    font-weight: bold;
}
</style>
"""
import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, Set, List

class VariableContext:
    def __init__(self):
        self.files: Set[str] = set()
        self.filters: Set[str] = set()
        self.examples: List[Dict] = []
        self.loop_contexts: Dict[str, Set[str]] = defaultdict(set)
        self.default_values: Set[str] = set()
        self.nested_patterns: Dict[str, Set[str]] = defaultdict(set)

def clean_example_content(content: str) -> str:
    """Clean up the example content by:
    1. Converting HTML entities back to tags
    2. Converting **var** to proper formatting
    3. Cleaning up code blocks
    """
    # Convert HTML entities back to tags
    content = content.replace('&lt;', '<').replace('&gt;', '>')
    
    # Convert **variable** to proper formatting
    # Use a regex to find {{variable}} patterns and format them appropriately
    content = re.sub(r'\*\*\{\{(.*?)\}\}\*\*', r'`{{\1}}`', content)
    
    # Clean up other bold markers that aren't variables
    content = re.sub(r'\*\*(.*?)\*\*', r'**\1**', content)
    
    return content

class TemplateAnalyzer:
    CSS_STYLES = """
    <!-- CSS styles remain unchanged -->
    """
    
    def __init__(self):
        self.variables: Dict[str, VariableContext] = defaultdict(VariableContext)
    
    def clean_template_content(self, content: str) -> str:
        return '\n'.join(
            line for line in content.split('\n')
            if line.strip() and line not in set()
        )
    
    def highlight_variable_in_context(self, context: str, var_name: str) -> str:
        pattern = r'({{\s*' + re.escape(var_name) + r'[^}]*}})'
        return re.sub(pattern, r'<span class="variable-highlight">\1</span>', context)

    def extract_context(self, content: str, var_match_start: int, window: int = 2) -> str:
        lines = content.split('\n')
        line_no = content[:var_match_start].count('\n')
        return '\n'.join(
            lines[max(0, line_no - window):min(len(lines), line_no + window + 1)]
        ).strip()
    
    def parse_filters(self, variable_token: str) -> List[str]:
        filters = re.findall(r'\|([\w:"]+)', variable_token)
        return [
            f"{f.split(':', 1)[0]} (arg: {f.split(':', 1)[1]})" if ':' in f else f
            for f in filters
        ]
    
    def analyze_file(self, file_path: str):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = self.clean_template_content(f.read())
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='latin-1') as f:
                content = self.clean_template_content(f.read())
        
        loop_contexts = {
            m.group(2): m.group(1)
            for m in re.finditer(r'{%\s*for\s+(\w+)\s+in\s+(\w+)', content)
        }
        
        for match in re.finditer(r'{{\s*([\w\.]+)(\s*\|[\w:"]+\s*)*\s*}}', content):
            full_var = match.group(0)
            var_path = match.group(1)
            parts = var_path.split('.')
            main_var = parts[0]
            
            var_info = self.variables[main_var]
            var_info.files.add(file_path)
            var_info.filters.update(self.parse_filters(full_var))
            
            context = self.extract_context(content, match.start())
            var_info.examples.append({
                "context": context,
                "template": full_var
            })
            
            for loop_var, iterator in loop_contexts.items():
                if main_var == iterator:
                    var_info.loop_contexts[loop_var].add(context)
            
            if len(parts) > 1:
                var_info.nested_patterns['.'.join(parts[1:])].add(full_var)
            
            if default_match := re.search(r'\|default:"([^"]+)"', full_var):
                var_info.default_values.add(default_match.group(1))
    
    def generate_markdown(self, output_file: str = "index.md"):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('---\n')
            f.write('title: Django Template Variables Documentation\n')
            f.write('layout: default\n')
            f.write('---\n\n')
            
            f.write(self.CSS_STYLES)
            
            f.write('# Django Template Variables Documentation\n\n')
            
            # Table of Contents
            f.write('## Table of Contents\n')
            for var_name in sorted(self.variables.keys()):
                f.write(f'- [{var_name}](#{var_name.lower()})\n')
            f.write('\n---\n\n')
            
            for var_name, var_info in sorted(self.variables.items()):
                if var_info.loop_contexts:
                    f.write(f'## {var_name}\n')
                    f.write('<div class="loop-info">')
                    f.write('Loop Iterator')
                    f.write('<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span>')
                    f.write('</div>\n\n')
                else:
                    f.write(f'## {var_name}\n\n')
                
                if var_info.default_values:
                    f.write('**Default values:** ' + 
                        ', '.join(f'`{v}`' for v in sorted(var_info.default_values)) + 
                        '\n\n')
                
                self._write_files_section(f, var_info)
                self._write_properties_section(f, var_info)
                self._write_filters_section(f, var_info)
                self._write_examples_section(f, var_info, var_name)
                
                f.write('---\n\n')

    def _write_files_section(self, f, var_info):
        f.write('<details class="expandable-section">\n')
        f.write('<summary><strong>Found in files</strong></summary>\n\n')
        for file_path in sorted(var_info.files):
            f.write(f'- {os.path.basename(file_path)}\n')
        f.write('\n</details>\n\n')

    def _write_filters_section(self, f, var_info):
        if var_info.filters:
            f.write('<details class="expandable-section">\n')
            f.write('<summary><strong>Filters Used</strong></summary>\n\n')
            for filter_name in sorted(var_info.filters):
                f.write(f'- `{filter_name}`\n')
            f.write('\n</details>\n\n')

    def _write_examples_section(self, f, var_info, var_name):
        if var_info.examples:
            f.write('<details class="expandable-section">\n')
            f.write('<summary><strong>Usage Examples</strong></summary>\n\n')
            
            seen_examples = set()
            for ex in var_info.examples:
                if ex["context"] in seen_examples:
                    continue
                
                cleaned_context = clean_example_content(ex["context"])
                if cleaned_context:
                    # Add raw tags around the entire code block
                    f.write('```django\n')
                    f.write(cleaned_context + '\n')
                    f.write('```\n\n')
                    seen_examples.add(ex["context"])
                
                if len(seen_examples) >= 3:
                    break
            
            f.write('</details>\n\n')

    def _write_properties_section(self, f, var_info):
        if var_info.nested_patterns:
            f.write('<details class="expandable-section">\n')
            f.write('<summary><strong>Properties</strong></summary>\n\n')
            f.write('| Property | Example Value |\n')
            f.write('|----------|---------------|\n')
            
            for pattern, examples in sorted(var_info.nested_patterns.items()):
                example = next(iter(examples))
                pattern = pattern.strip().replace('|', '\\|')
                example = example.strip().replace('|', '\\|')
                pattern = pattern.replace('`', '')
                example = example.replace('`', '')
                
                # Escape Django template syntax in the example
                example = example.replace('{{', '{%raw%}{{').replace('}}', '}}{%endraw%}')
                
                f.write(f'| `{pattern}` | `{example}` |\n')
            
            f.write('\n')
            f.write('</details>\n\n')

def main():
    analyzer = TemplateAnalyzer()
    input_path = Path('/Users/joe/Documents/Scripts/Variable Extractor/generic')
    
    for file_path in input_path.rglob('*'):
        if file_path.is_file():
            print(f"Processing: {file_path}")
            analyzer.analyze_file(str(file_path))
    
    analyzer.generate_markdown()
    print("Documentation generated successfully!")

if __name__ == "__main__":
    main()