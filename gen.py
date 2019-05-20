#!/usr/bin/env python

print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>ASCII table and history (or, why does Ctrl+i insert a Tab?)</title>
    <link rel="canonical" href="https://bestasciitable.com">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato:400,700&amp;subset=latin-ext">
    <link rel="shortcut icon" href="/favicon.ico">
    <style>
        *          { box-sizing: border-box; }
        html       { font: 16px/140% Lato, sans-serif; background-color: #f7f7f7; }
        body       { margin: 0; display: flex; flex-direction: column; align-items: center; }
        header     { text-align: center; width: 100%; background-color: #ebe7c3; padding-bottom: 1em; }
        h1         { margin-bottom: .2em; }
        h2         { background-color: #ebe7c3; width: 100%; text-align: center; padding: .5em 0; margin-top: .5em;  }
        h3         { margin: 0; }
        h3 + p     { margin-top: 5px; }
        #intro     { max-width: 60em; display: flex; }
        img        { cursor: pointer; }
        figure     { max-width: 300px; background-color: #fff; color: #333; border: 1px solid #ddd; border-radius: 2px; margin-right: 0; }
        figcaption { padding: 0 6px; padding-bottom: 4px; }
        table      { font: 16px/100% monospace; border-collapse: collapse; display: flex; justify-content: flex-start; max-width: 100%; overflow-x: auto; }
        tbody      { padding: 0 10px; border-right: 1px solid #888; }
        tbody:last-child { border-right: none; }
        td         { padding: 6px; }
        tr         { border-top: 1px solid #888; }
        footer     { background-color: #ebe7c3; padding: 1em; margin-top: 1em; width: 100%; }
        footer p   { margin: .5em 0; }
        a          { text-decoration: none; color: #00f; transition: color .2s; }
        a:hover    { text-decoration: underline; color: #6491ff; }
        li         { margin-bottom: .4em; }

        p, li, figcaption { text-align: justify; hyphens: auto; }
        tr:nth-child(1)   { border-top: none; }

        td:nth-child(1)   { color: #cd0000; }
        td:nth-child(2)   { }
        td:nth-child(3)   { color: #008787; white-space: nowrap; }
        td:nth-child(4)   { font-weight: bold; text-align: right; }

        img.imgzoom-loading { cursor: wait; }
        .imgzoom-large      { cursor: pointer; box-shadow: 0 0 8px rgba(0, 0, 0, .3); transition: all .4s; }

        @media (max-width: 62em) {
            #intro { padding: 0 1em; }
            figure { margin-left: 1em; }
            table  { margin: 0 1em; }
        }

        @media (max-width: 45em) {
            img { max-width: 250px; }
        }

        @media (max-width: 40em) {
            img    { width: 100%; }
            figure { width: 48%; margin-left: .5%; }
            #intro { display: block; }
            #intro-img {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
            }
        }
    </style>
</head>

<body>
    <header>
        <h1>ASCII table and history</h1>
        <strong>Or, why does Ctrl+i insert a Tab?</strong>
    </header>

    <h2 style="margin-bottom: 0">Introduction</h2>
    <div id="intro">
        <div>
            <p>To understand why Control+i inserts a tab you need to understand
            ASCII, and to understand ASCII you need know a bit about its history
            and the world it was developed in. Please bear with me (or <a
            href="#table">just go the table</a>).</p>

            <h3 id="teleprinters">Teleprinters</h3>
            <p>Teleprinters evolved from the telegraph. Connect a printer and
            keyboard to a telegraph and you’ve got a teleprinter. Early versions
            were called “printing telegraphs”.</p>

            <p>Teleprinters communicated using ITA2. For the most part this was
            just a standard to encode the alphabet, but there are a few control
            codes: WRU (“Who R U”) would cause the receiving teletype to send
            back its identification, BEL would ring a bell, and the familiar CR
            (Carriage Return) and LF (Line Feed).</p>

            <p>This is all early 20th century stuff. There are no computers;
            it’s all mechanical working with punched tape. ITA2 (and codes like
            it) were mechanical efficient; common letters such as “e” and “t”
            required only a single hole to be punched.</p>

            <p>These 5-bit codes could only encode 32 characters, which is not
            enough. The solution was to add the FIGS and LTRS codes, which would
            switch between “figures” and “letters” mode. “FIGS R W” would
            produce “42”. This worked, but typo’ing a FIGS or LTRS, or losing
            one in line noise, would result in gibberish. Not ideal.</p>

            <h3 id="terminals">Terminals</h3>

            <p>Teleprinters were also used to connect to computers, rather than
            other teleprinters. ITA2 was designed for mechanical machines and
            awkward, so ASCII designed specifically for computer use and
            published in 1962. Teleprinters used with computers were called
            <em>terminals</em> (as in “end of a connection”, like “train
            terminal”).</p>

            <p>It’s perhaps hard to imagine, but people really programmed computers
            using Teletypes. Here’s a
            <a href="https://www.youtube.com/watch?v=qv5b1Xowxdk">video of a teleprinter in action</a>,
            and here’s a cheesy (but interesting and cute) video which explains
            how they
            <a href="https://www.youtube.com/watch?v=XV-7J5y1TQc">were used to program a PDP 11/10</a>.
            </p>

            <p>The Teletype model 33 was massively popular, and the brand name
            Teletype became synonymous with terminal. The abbreviated form of
            Teletype is TTY. Yes, like /dev/tty or /bin/stty on your modern
            Linux or macOS system.</p>

            <p>A terminal would connect to a computer using a serial port (<a
            href="https://en.wikipedia.org/wiki/RS-232">RS-232</a>) which
            simply transferred characters. The best way to see a terminal is as
            a monitor with an integrated keyboard, rather than a computer on its
            own. A modern monitors connected with HDMI is told “draw this pixel
            in this colour”. In the 1960s the computer merely said “draw this
            character”.</p>

            <p>Teleprinters and terminals connected with <em>only</em> a serial
            port sending characters, so they needed some way to communicate
            events such as “stop sending me data” or “end of transmission”. This
            is what control characters are for. The exact meaning of control
            characters has varied greatly over the years (which is why extensive
            <a href="https://en.wikipedia.org/wiki/Termcap">termcap
            databases</a> are required). ASCII is more than just a character
            set; it’s a way to communicate between a terminal and a
            computer.</p>

            <p>An additional method to communicate which came along with visual
            terminals like the ADM-3A and VT100 is sending <em>escape
            sequences</em>. This is a list of characters starting with the ESC
            control character (0x1b) which have a special meaning.

            For example F1 is “&lt;Esc&gt;OP”,
            the left arrow is “&lt;Esc&gt;[OD”,
            “&lt;Esc&gt;[2C” is move the cursor 2 positions forward, 
            “&lt;Esc&gt;[4m” underlines all subsequent text,
            etc. </p>

            <h3 id="modern">Modern systems and ASCII properties</h3>
            <p>All of this matters because modern terminals operate on the same
            fundamentals as those of the 60s. If you’re opening three windows
            with xterm or iTerm2 then you’re emulating three terminals
            connecting to a “mainframe”.</p>

            <p>If you look at the ASCII table below then there are some
            interesting properties: in the 1st column you can see how the left
            two bits are always set to zero, and that the rest count to 31 (32
            characters in total; it starts at 0). The 2nd column then repeats
            this pattern but with the 5th bit set to 1 (remember, read binary
            numbers from right-to-left, so that’s 5th from the right). The
            3rd column repeats this pattern again with the 6th bit set, and the
            final column has both bits set.</p>

            <p>The interesting part here is that the letters A-Z, as well as
            some punctuation, map directly to the control characters in the
            first column. All that’s needed is removing one bit, and that’s
            exactly what the Control key did: clear the 6th bit. Lowercase and
            uppercase letters align in the 3rd and 4th columns, and this is what
            the Shift key did: clear the 5th bit.</p>

            <p>Pressing Control+a (lowercase) would mean sending !, which is not
            very useful. So most terminals interpret this as Control+A
            (uppercase), which sends SOH.</p>

            <p>DEL is last is because all bits are set to 1. This is how you
            “deleted” a character in punch tapes: punch all the holes!</p>

            <p>This is kind of neat and well designed, but it does have some
            effects, even for modern terminals:</p>

            <ul>
                <li>There is no way to see if the user pressed just Control or
                Shift, because from a terminal’s perspective all they do is
                modify a bit for the typed character.</li>

                <li>There is no way to distinguish between the Tab key and
                Control+i. It’s not just ‘the same’ as Tab, Control+i
                <strong>is</strong> Tab.</li>

                <li>There is no way to distinguish between Control+a and
                Control+Shift+a.</li>

                <li>Sending Control with a character from the 2nd column is
                useless. Control removes the 7th bit, but this is already 0, so
                Control+: will just send : (this does work for some characters
                now, but not all)</li>
            </ul>

            <p>The world has not <em>completely</em> stood still, and there are
            some improvements from the 1960s, but terminals are still
            fundamentally ASCII-based text interfaces, and programs running
            inside a terminal – like a shell or Vim – still have very limited
            facilities for modern key events. Non-terminal programs don’t have
            these problems as they’re not restricted to a 1960s text
            interface.</p>

            <p style="font-size: 12px; border-top: 1px solid #333;">Note: for
            brevity’s sake many details have been omitted in the above: ITA2 was
            derived from Murray code, the 1967 ASCII spec changed many aspects
            (1962 ASCII only had uppercase), there were other encodings (e.g.
            EBCDIC), graphical terminals such as the Tektronix 4014 (which xterm
            can emulate), ioctls, etc.</p>
        </div>

        <div id="intro-img">
            <figure>
                <img src="printing-telegraph-t.jpg" data-large="printing-telegraph.jpg" alt="Stock Exchange printing telegraph, 1907">
                <figcaption><em>Image 1</em>, a printing telegraph produced in
                1907. The alphabetically sorted piano-style keys are a great
                example of how the first generation of a new innovation tends to
                resemble whatever already exists, and that it takes a few more
                innovations to really get the most out of it (this style of
                piano keyboards was introduced in the 1840s, and while the
                keyboard as we know it today was introduced in the 1870s, it
                took a while for it to replace all piano-style keyboards; this
                is probably among the last models that was made).
                </figcaption>
            </figure>
            <figure>
                <img src="tty-model-33-asr-t.jpg" data-large="tty-model-33-asr.jpg" alt="Teletype model 33 ASR, 1963">
                <figcaption><em>Image 2</em>, the Teletype model 33 ASR,
                introduced in 1963. This is one first ASCII teleprinters. Note
                the machinery on the left; you could feed this with a punched
                tape to automatically type a program for you, similar to how you
                would now load a program from a disk.
                </figcaption>
            </figure>
            <figure>
                <img src="pdp11-t.jpg" data-large="pdp11.jpg" alt="Ken Thompson working on the PDP-11">
                <figcaption><em>Image 3</em>, Ken Thompson working on the PDP-11
                using a Teletype. What always struck be about this image is the
                atrocious ergonomics of … everything. The keyboard, the chair,
                everything about the posture: it’s all terrible. Inventing Unix
                almost seems <em>easy</em> compared to dealing with
                that!</figcaption>
            </figure>
            <figure>
                <img src="vt100-t.jpg" data-large="vt100.jpg" alt="DEC VT-100">
                <figcaption><em>Image 4</em>, DEC VT100, a kind of terminal that
                a terminal emulator such as xterm emulates. It has a visual
                display and supports the essential escape sequences.</figcaption>
            </figure>
        </div>
    </div>

    <h2>The table</h2>
    <table id="table">''')


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
        print('        </tbody>')

    if n == 0 or n == 0x20 or n == 0x40 or n == 0x60:
        print('''        <tbody>
            <tr>
                <th>Dec</th>
                <th>Hex</th>
                <th>Binary</th>
                <th>Char</th>
            </tr>''')

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
    print(f'''
            <tr>
                <td>{n}</td>
                <td>{hex(n)}</td>
                <td>{b[:2]} {b[2:]}</td>
                <td{' title="' + title + '"' if title else ''}>{char}</td>
            </tr>''')
print('''
            </tbody>
        </table>

        <div>
            <p style="text-align: center">The binary representation has the most significant bit first
            ("big endian").<br>

            ASCII is 7-bit; because many have called encodings such as 
            <a href="https://en.wikipedia.org/wiki/Code_page_437">CP437</a>,
            <a href="https://en.wikipedia.org/wiki/ISO/IEC_8859-1">ISO-8859-1</a>,
            <a href="https://en.wikipedia.org/wiki/Windows-1252">CP-1252</a>,
            and others “extended ASCII” some are under the misapprehension that
            ASCII is 8-bit (1 byte).</p>
        </div>

        <footer>
            <p>Created by <a href="https://arp242.net">Martin Tournoij</a>,
            because I’ve had to explain “Control + i *is* Tab” once too many
            times and figured an in-depth explanation would be helpful.</p>

            <p><a href="https://github.com/arp242/bestasciitable">Source on GitHub</a>;
            PRs and issues welcome.</p>

            <p>
                Image credits:
                <a href="http://collection.sciencemuseum.org.uk/objects/co33749/stock-exchange-printing-telegraph-1907-telegraph">
                    Image 1 by Science Museum</a>; <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA</a> |
                <a href="https://en.wikipedia.org/wiki/File:Teletype_with_papertape_punch_and_reader.jpg">
                    Image 2 by AlisonW</a>; <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">CC BY-SA</a> |
                <a href="https://en.wikipedia.org/wiki/File:Ken_Thompson_(sitting)_and_Dennis_Ritchie_at_PDP-11_(2876612463).jpg">
                    Image 3 by Peter Hamer</a>; <a href="https://creativecommons.org/licenses/by-sa/2.0/deed.en">CC BY-SA</a> |
                <a href="https://www.flickr.com/photos/54568729@N00/9636183501">
                    Image 4 by Jason Scott</a>; <a href="https://creativecommons.org/licenses/by/2.0/">CC BY</a>
            </p>

            <p>References and further reading:
                <a href="https://worldpowersystems.com/ARCHIVE/codes/">An annotated history of some character codes</a> |
                <a href="https://www.aivosto.com/articles/charsets-7bit.html">7-bit character sets</a> |
                <a href="https://www.aivosto.com/articles/control-characters.html">Control characters in ASCII and Unicode</a> |
                <a href="http://www.linusakesson.net/programming/tty/">The TTY demystified</a>
            </p>
        </footer>

        <script src="imgzoom.js"></script>
        <script>
            window.addEventListener('load', function() {
                var img = document.querySelectorAll('img');
                for (var i=0; i<img.length; i++)
                    img[i].addEventListener('click', function(e) { imgzoom(this); }, false);
            }, false);
        </script>
    </body>
</html>''')
