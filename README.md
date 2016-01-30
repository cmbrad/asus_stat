# Asus Stat

## Description
Python package designed for getting information such as SNR and line rate from ASUS routers.  

## Supported Devioces
* DSL-AC68U  

## Example Usage

```
from asus_stat.devices import DSLAC68U

d = DSlAC68U(host='192.168.1.1', port=22, username='admin', password='admin')
print('SNR (downstream) {}'.format(d.dsl_snr_margin_down()))
```

