from charms.reactive import RelationBase
from charms.reactive import hook


class LogstashProvider(RelationBase):

    @hook('{provides:logstash-client}-relation-{joined,changed}')
    def joined_changed(self):
        # Notify that we have an incoming request for data
        self.set_state('{relation_name}.connected')

    @hook('{provides:logstash-client}-relation-{departed,broken}')
    def departed_broken(self):
        self.remove_state('{relation_name}.connected')

    def provide_data(self, tcp_port, udp_port):
        for conv in self.conversations():
            self.set_remote(scope=conv.scope, data={'tcp_port': tcp_port,
                                                    'udp_port': udp_port})
