#!/usr/bin/env python

out = None
i = 0
with open('pres_tmp.html','r') as f:
    for line in f:
        if 'class="slide"' in line:
            print('</html>',file=out)
            try:
                out.close()
            except:
                pass
            i += 1
            out = open('slides/{:02d}.html'.format(i),'w')
            with open('head.html','r') as h:
                for l in h:
                    print(l,file=out,end='')
        print(line,file=out,end='')
