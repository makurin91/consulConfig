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


def import_config_consul():
    os.system('docker run --rm -v ${PWD}:/app -w /app --network'
              f' host consul kv import -http-addr={consul_host}:8500 @{file_name}')


def encode_base_format():
    with open(decoded_file) as f:
        text = f.read()
        d = json.loads(text)
        new_list = []
        for i in d:
            cs_keys = dict(i).get('key')
            cs_values = dict(i).get('value')
            enc_utf = cs_values.encode('utf-8')
            enc_base = base64.b64encode(enc_utf)
            decode_values = enc_base.decode('utf-8')
            line = {'key': cs_keys, 'flags': 0, 'value': decode_values}
            new_list.append(line)
        formated_file = json.dumps(new_list, indent=4)
        with open(file_name, mode="w") as f:
            f.write(formated_file)

if __name__ == "__main__":
    check_docker_life()
    encode_base_format()
    time.sleep(3)
    import_config_consul()