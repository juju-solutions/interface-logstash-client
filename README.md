# Interface logstash-client

This interface layer is used for connecting to a logstash unit over TCP or UDP.

## States

`{relation_name}.connected` - The relationship has been established, but not enough data has been sent to determine if we are ready to configure the client.

`{relation_name}.available` - We have the required information, we can now configure our consumer service.

### Examples

When implementing this interface as a requirer:

`metadata.yaml`

     requires:
         logstash:
             interface: logstash-client


`layer.yaml`

    includes: ['interface:logstash-client']

`reactive/thing.py`

    @when('logstash.available')
    def start_up_logger(logstash):
        start_logger(logstash.private_address(), logstash.tcp_port())

### Data

Logstash send's clients the following information, per host

 - tcp_port - default: 6000
 - udp_port - default: 5000
 - private-address

### Maintainers

- Charles Butler &lt;charles.butler@canonical.com&gt;
- Matt Bruzek &lt;matthew.bruzek@canonical.com&gt;
