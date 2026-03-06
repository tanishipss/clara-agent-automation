from deepdiff import DeepDiff


def generate_diff(old_config, new_config):

    diff = DeepDiff(old_config, new_config, ignore_order=True)

    return diff