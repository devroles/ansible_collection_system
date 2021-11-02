def etc_hosts_name(value):
    domains = value.split(".")
    names = [value]
    for i in range(1, len(domains)):
        names.append(".".join(domains[:i]))
    return " ".join(names)


class FilterModule(object):
    def filters(self):
        return {"etc_hosts_name": etc_hosts_name}
