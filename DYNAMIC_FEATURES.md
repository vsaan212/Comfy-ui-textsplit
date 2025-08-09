# Dynamic Output Features

## Overview
The Text Split node now includes dynamic output functionality inspired by the [ComfyUI-Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack). The GUI automatically updates to show only the relevant outputs based on the `num_splits` parameter.

## Key Improvements

### ✅ **Dynamic GUI Updates**
- **Before**: Always showed 8 text outputs regardless of `num_splits` setting
- **After**: GUI dynamically shows only `num_splits` + 1 outputs (including remainder)

### ✅ **Remainder Output**
- **Before**: Extra content was lost or ignored
- **After**: All remaining content after `num_splits` is collected in a "remainder" output

### ✅ **Smart Output Management**
- **Active outputs**: Only the first `num_splits` outputs are visible and contain data
- **Remainder output**: Always visible and contains any leftover content
- **Unused outputs**: Hidden in GUI but still available for connection

## How It Works

### JavaScript Integration
The `text_split_dynamic.js` file provides the dynamic GUI functionality:
- Monitors changes to the `num_splits` parameter
- Automatically updates output visibility
- Maintains proper output naming and connections

### Python Backend
The `text_split_node.py` handles the logic:
- Splits text into the specified number of parts
- Collects remaining content into the remainder output
- Returns consistent output structure for ComfyUI

## Usage Examples

### Example 1: 2 Splits
```
Input: "Scene 1|Scene 2|Scene 3"
Num Splits: 2
GUI Shows: text_1, text_2, remainder
Output:
  text_1: "Scene 1"
  text_2: "Scene 2"
  remainder: "Scene 3"
```

### Example 2: 5 Splits
```
Input: "A|B|C|D|E|F|G"
Num Splits: 5
GUI Shows: text_1, text_2, text_3, text_4, text_5, remainder
Output:
  text_1: "A"
  text_2: "B"
  text_3: "C"
  text_4: "D"
  text_5: "E"
  remainder: "F|G"
```

### Example 3: 1 Split
```
Input: "Single|Part"
Num Splits: 1
GUI Shows: text_1, remainder
Output:
  text_1: "Single"
  remainder: "Part"
```

## Technical Implementation

### Dynamic Output Logic
1. **Text Processing**: Split input text using specified separator
2. **Main Parts**: Take first `num_splits` parts as individual outputs
3. **Remainder**: Join all remaining parts with the original separator
4. **GUI Update**: JavaScript hides unused outputs and shows active ones

### Benefits
- **Cleaner Interface**: Only relevant outputs are visible
- **No Data Loss**: All content is preserved in outputs
- **Flexible Usage**: Easy to adjust number of splits without reconnecting
- **Consistent Behavior**: Works reliably across different input scenarios

## Compatibility

- **ComfyUI**: Fully compatible with ComfyUI's node system
- **Python**: Works with Python 3.7+
- **Dependencies**: No external dependencies required
- **Performance**: Minimal overhead, efficient processing

## Future Enhancements

The dynamic output system provides a foundation for additional features:
- **Custom Output Names**: Allow user-defined output names
- **Advanced Remainder Handling**: Options for remainder processing
- **Batch Processing**: Support for multiple input streams
- **Conditional Outputs**: Show/hide outputs based on content

This implementation follows the same patterns used in the ComfyUI-Inspire-Pack, ensuring consistency and reliability in the ComfyUI ecosystem.
