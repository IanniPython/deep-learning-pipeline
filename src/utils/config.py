import yaml


with open('default.yaml', 'r') as f:
    data = yaml.safe_load(f)

print(data['train'])



    