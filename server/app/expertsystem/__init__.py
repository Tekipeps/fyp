import yaml


def parse_conditions(kb, table):
    inference = ""
    for attribute in kb:
        attrname = list(attribute.keys())[0]
        for condition in attribute[attrname]["conditions"]:
            if condition.startswith(">"):
                val = int(condition[1:])
                if table[attrname] > val:
                    inference += attribute[attrname]["messages"][condition]
            elif condition.startswith("<"):
                val = int(condition[1:])
                if table[attrname] < val:
                    inference += attribute[attrname]["messages"][condition]
            elif condition == "True":
                if table[attrname] == True:
                    inference += attribute[attrname]["messages"][condition]
            elif condition == "False":
                if table[attrname] == False:
                    inference += attribute[attrname]["messages"][condition]
    return inference


def load_kb():
    kb = ""
    with open("kb.yaml", "r") as stream:
        try:
            kb = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise exc
    return kb


def get_inference(restingbp, fbs, cholesterol):
    # lookup table
    table = { "restingbp": restingbp, "fbs": fbs, "cholesterol": cholesterol}
    
    kb = load_kb()

    inference = parse_conditions(kb, table)

    return inference
