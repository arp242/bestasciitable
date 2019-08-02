#!/usr/bin/env python

names = ['NUL', 'SOH', 'STX', 'ETX', 'EOT', 'ENQ', 'ACK', 'BEL', 'BS', 'HT',
         'LF', 'VT', 'FF', 'CR', 'SO', 'SI', 'DLE', 'DC1', 'DC2', 'DC3',
         'DC4', 'NAK', 'SYN', 'ETB', 'CAN', 'EM', 'SUB', 'ESC', 'FS', 'GS',
         'RS', 'US', 'SPACE']

titles = ['\\0, null character', 'start of heading', 'start of text',
          'end of text', 'end of transmission', 'enquiry', 'acknowledge',
          '\\a, bell', '\\b, backspace', '\\t, horizontal tab',
          '\\n, new line', '\\v, vertical tab', '\\f, form feed',
          '\\r, carriage ret', 'shift out', 'shift in', 'data link escape',
          'device control 1', 'device control 2', 'device control 3',
          'device control 4', 'negative ack.', 'synchronous idle',
          'end of trans. blk', 'cancel', 'end of medium', 'substitute',
          'escape', 'file separator', 'group separator', 'record separator',
          'unit separator']

for n in range(0, 128):
    if n == 0x20 or n == 0x40 or n == 0x60:
        print('</tbody>')

    if n == 0 or n == 0x20 or n == 0x40 or n == 0x60:
        print('''<tbody>
    <tr><th>Dec</th><th>Hex</th><th>Binary</th><th>Char</th></tr>''')

    char = chr(n)
    if n <= 0x20:
        char = names[n]
    elif char == '<':
        char = '&lt;'
    elif char == '>':
        char = '&gt;'
    elif char == '&':
        char = '&amp;'
    elif n == 127:
        char = 'DEL'

    title = ''
    if n < 0x20:
        title = titles[n]

    b = f'{n:0>7b}'
    print(f'''    <tr><td>{n}</td><td>{hex(n)}</td><td>{b[:2]} {b[2:]}</td><td{' title="' + title + '"' if title else ''}>{char}</td></tr>''')
print('</tbody>')
