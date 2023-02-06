import os
import json
import base64
import time

consul_host = "consul_address"
file_name = "consulDump.json"
decoded_file = "decodeDump.json"


def check_docker_life():
    a = os.system('docker info')
    assert a == 0, "Docker is not enabled"


def export_config_consul():
    os.system(f'docker run --rm consul kv export -http-addr={consul_host}:8500 > {file_name}')


def decode_base_format():
    with open(file_name) as f:
        text = f.read()
        d = json.loads(text)
        new_list = []
        for i in d:
            cs_keys = dict(i).get('key')
            cs_values = dict(i).get('value')
            data = base64.b64decode(cs_values)
            decode_values = data.decode('utf-8')
            line = {'key': cs_keys, 'flags': 0, 'value': decode_values}
            new_list.append(line)
        formated_file = json.dumps(new_list, indent=4)
        with open(decoded_file, mode="w") as f:
            f.write(formated_file)
        os.remove(file_name)

if __name__ == "__main__":
    check_docker_life()
    export_config_consul()
    time.sleep(5)
    decode_base_format()