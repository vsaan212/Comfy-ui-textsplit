# ComfyUI Text Split Node

A custom ComfyUI node that splits text into multiple outputs for feeding complex multi-scene renders. This node allows you to dynamically control the number of splits and use custom separators.

## Features

- **Single Text Input**: Accepts any text input for splitting
- **Custom Separators**: Use any string or regex pattern as a separator
- **Dynamic Output Count**: Control the number of splits (1-8 outputs)
- **Text Processing Options**: Trim whitespace and remove empty parts
- **Regex Support**: Use regex patterns for advanced splitting

## Installation

### Automatic Installation
1. Run the `install.bat` script to check dependencies and install the node
2. Copy this folder to your ComfyUI `custom_nodes` directory
3. Restart ComfyUI

### Manual Installation
1. Copy this folder to your ComfyUI `custom_nodes` directory
2. Install any dependencies listed in `requirements.txt` (if any)
3. Restart ComfyUI

## Usage

### Basic Usage
1. Add the "Text Split" node from the "text" category
2. Connect your text input to the node
3. Configure the separator (default: `|`)
4. Set the number of splits (1-8)
5. Connect the outputs to other nodes

### Input Parameters

- **text**: The input text to split (multiline supported)
- **separator**: Custom separator string or regex pattern
  - Simple string: `|`, `,`, `;`, etc.
  - Regex pattern: `/pattern/` (e.g., `/\\s+/` for multiple spaces)
- **num_splits**: Number of splits to create (1-8)
- **trim_whitespace**: Whether to trim whitespace from split parts
- **remove_empty**: Whether to remove empty parts

### Outputs

The node provides dynamic text outputs based on the `num_splits` parameter:
- `text_1` through `text_n` (where n = num_splits)
- `remainder` - Contains any leftover text after the specified number of splits

**Dynamic Behavior:**
- When `num_splits` is 2: Shows `text_1`, `text_2`, and `remainder`
- When `num_splits` is 5: Shows `text_1`, `text_2`, `text_3`, `text_4`, `text_5`, and `remainder`
- Unused outputs are hidden in the GUI but still available for connection

## Examples

### Example 1: Simple Split
```
Input: "Scene 1|Scene 2|Scene 3"
Separator: "|"
Num Splits: 2
Output: 
  text_1: "Scene 1"
  text_2: "Scene 2"
  remainder: "Scene 3"
```

### Example 2: Regex Split
```
Input: "Scene 1   Scene 2   Scene 3"
Separator: "/\\s+/"
Num Splits: 2
Output:
  text_1: "Scene 1"
  text_2: "Scene 2"
  remainder: "Scene 3"
```

### Example 3: Multi-scene Prompt with Remainder
```
Input: "A beautiful sunset|A stormy night|A peaceful morning|A dark forest"
Separator: "|"
Num Splits: 3
Output:
  text_1: "A beautiful sunset"
  text_2: "A stormy night"
  text_3: "A peaceful morning"
  remainder: "A dark forest"
```

## Use Cases

- **Multi-scene Renders**: Split complex prompts into individual scene descriptions
- **Batch Processing**: Process multiple text inputs simultaneously
- **Conditional Prompts**: Create variations of prompts for different scenarios
- **Text Analysis**: Split text for further processing by other nodes

## Technical Details

- **Category**: text
- **Input Types**: STRING, INT, BOOLEAN
- **Output Types**: STRING (up to 8 outputs)
- **Dependencies**: None (uses Python standard library only)
- **Minimum Python Version**: 3.7
- **Compatibility**: Python 3.7+ (all versions above minimum supported)

## Troubleshooting

### Node Not Appearing
- Ensure the folder is in the correct `custom_nodes` directory
- Restart ComfyUI completely
- Check the console for any error messages

### Incorrect Splitting
- Verify your separator string is correct
- For regex patterns, ensure they start and end with `/`
- Check that `num_splits` is set to the desired number

### Empty Outputs
- Ensure your input text contains the separator
- Check that `remove_empty` is not removing valid content
- Verify `num_splits` is not set higher than the number of parts

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.
