# -*- coding: utf-8 -*-
"""작은 모사 그림 조각들. 상태 띠·사례·플랫폼 칸에서 쓴다."""
W = {"4": "40", "6": "60", "8": "80"}

def mini(inner="", bars="684", tall=True, label="", style=""):
    bb = "".join('<div class="mini__bar mini__bar--w%s"></div>' % W[c] for c in bars)
    return ('              <div class="mini%s" role="img" aria-label="%s"%s>'
            '<div class="mini__bg">%s</div>%s</div>'
            ) % (" mini--tall" if tall else "", label, (' style="%s"' % style) if style else "", bb, inner)

def toast(msg, act="되돌리기", style=""):
    a = '<b>%s</b>' % act if act else ""
    return '<div class="mini__toast"%s>%s%s</div>' % ((' style="%s"' % style) if style else "", msg, a)

def trigger(label="삭제", top="8px"):
    return '<div style="margin-top:%s"><span class="mini__trigger">%s</span></div>' % (top, label)

def sheet(title, items, grab=True, scrim=True, style=""):
    li = "".join('<i>%s</i>' % x for x in items)
    inner = ('<div class="mini__sheet"%s>%s<b>%s</b>%s</div>'
             % ((' style="%s"' % style) if style else "", '<span class="grab"></span>' if grab else "", title, li))
    if scrim:
        return '<div class="mini__scrim" style="padding:0;place-items:end stretch">%s</div>' % inner
    return inner

def drawer(title, items, side="left", scrim=True):
    li = "".join('<i%s>%s</i>' % (' class="on"' if i == 0 else "", x) for i, x in enumerate(items))
    st = "" if side == "left" else ' style="left:auto;right:0;border-radius:6px 0 0 6px"'
    inner = '<div class="mini__drawer"%s><b>%s</b>%s</div>' % (st, title, li)
    if scrim:
        return '<div class="mini__scrim" style="padding:0">%s</div>' % inner
    return inner

def pop(items, pos="left:24px;top:40px", tail="left:10px;top:-4px", head=""):
    li = "".join('<i>%s</i>' % x for x in items)
    h = '<b style="font-size:8.5px;display:block;margin-bottom:2px">%s</b>' % head if head else ""
    return ('<div class="mini__pop" style="%s;width:78px"><span class="tail" style="%s"></span>%s%s</div>'
            % (pos, tail, h, li))

def tip(text, pos="left:16px;top:26px"):
    return '<div class="mini__tip" style="%s">%s</div>' % (pos, text)

def phone(inner, label=""):
    return ('              <div class="phone" role="img" aria-label="%s">'
            '<span class="phone__notch"></span><span class="phone__home"></span>'
            '<div class="phone__screen">%s</div></div>') % (label, inner)
