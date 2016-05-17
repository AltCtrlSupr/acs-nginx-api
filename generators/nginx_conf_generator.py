class NginxConfGenerator():
    def write_file(filename, data):
        with open(filename, 'w') as wfile:
            wfile.write(data)
            wfile.close()
            return True
        return False

    def read_file(filename):
        if os.path.isfile(filename):
            with open(filename, 'r') as data:
                return data.read()
        return None


