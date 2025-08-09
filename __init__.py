from .text_split_node import TextSplitNode

NODE_CLASS_MAPPINGS = {
    "TextSplit": TextSplitNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextSplit": "Text Split"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
