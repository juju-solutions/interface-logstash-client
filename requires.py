from charms.reactive import RelationBase
from charms.reactive import hook


class LogstashClient(RelationBase):

    auto_accessors = ['tcp_port', 'udp_port']

    @hook('{requires:logstash-client}-relation-{joined,changed}')
    def joined_changed(self):
        # Notify that we have an incoming request for data
        self.set_state('{relation_name}.connected')
        if self.get_remote('tcp_port') or self.get_remote('udp_port'):
            self.set_state('{relation_name}.available')

    @hook('{requires:logstash-client}-relation-{departed,broken}')
    def departed_broken(self):
        self.remove_state('{relation_name}.connected')
        self.remove_state('{relation_name}.available')

    def private_address(self):
        return self.get_remote('private-address')
