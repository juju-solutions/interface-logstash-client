# Interface logstash-client

This is a Juju charm interface layer. This interface is used for
connecting to a logstash unit over TCP or UDP.

## States

`{relation_name}.connected` - The relationship has been established, but not
enough data has been sent to determine if we are ready to configure the client.

`{relation_name}.available` - We have the required information, we can now
configure our consumer service.

### Examples

#### requires
Most charms will want to implement this interface as a client connection.
When implementing this interface as a requirer:

`metadata.yaml`
```yaml
  requires:
    logstash:
      interface: logstash-client
```

`layer.yaml`
```yaml
includes: ['interface:logstash-client']
```

`reactive/thing.py`
```python
  @when('logstash.available')
  def start_up_logger(logstash):
      start_logger(logstash.private_address(), logstash.tcp_port())
```

#### provides
The logstash charm provides this interface. If you wanted to provide this
interface in another layer:

`metadata.yaml`
```yaml
  provides:
    client:
      interface: logstash-client
```

`layer.yaml`
```yaml
includes: ['interface:logstash-client']
```

`reactive/code.py`
```python
  @when('client.connected')
  def configure_logstash_input(client):
    tcp_port = 6000
    udp_port = 5000
    client.provide_data(tcp_port, udp_port)
    # Write the logstash configuration with the TCP and UDP ports.
    configure_logstash(tcp_port, udp_port)
```

### Data

Logstash send's clients the following information, per unit

 - tcp_port - default: 6000
 - udp_port - default: 5000
 - private-address

### Maintainers

- Charles Butler &lt;charles.butler@canonical.com&gt;
- Matt Bruzek &lt;matthew.bruzek@canonical.com&gt;
