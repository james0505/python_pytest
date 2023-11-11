""" This is "conftest.py" file"""
import logging
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
console_handler =logging.StreamHandler()
logger.addHandler(console_handler)

def pytest_collection_modifyitems(config, items):
    """Add marker and custom test id to the test results

    Args:
        config (_type_): _description_
        items (_type_): _description_
    """
    for item in items:
        marker_names = [marker.name for marker in item.own_markers]
        if marker_names:
            if "test_id" in marker_names:
                marker_names.remove("test_id") # Won't add test_id name in the nodeis
            # Create a modified nodeid by adding marker names to the original nodeid
            if len(marker_names) > 0:
                modified_nodeid = f"{item.nodeid}::[{'_'.join(marker_names)}]"
                item._nodeid =modified_nodeid
        # Add test_id value in the nodeid
        for marker in item.iter_markers(name="test_id"):
            test_id = marker.args[0]
            #item.user_properties.append(("test_id", test_id))
            item._nodeid = f"{item.nodeid} [{''.join(test_id)}]"
