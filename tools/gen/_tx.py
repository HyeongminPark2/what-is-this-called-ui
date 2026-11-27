# -*- coding: utf-8 -*-
"""남은 부 카드에서 같이 쓰는 조각."""

def one(inner, tag="", ok=None, note="", w="152px"):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + col + ';border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:4px">'
            + ('<span style="font-size:8px;font-weight:700;color:' + col + '">' + tag + '</span>' if tag else '')
            + inner + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

def code(lines, w="152px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--fg-muted)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="font-family:var(--mono);font-size:9px;color:' + col + ';line-height:1.7;'
            'border:1px solid var(--line);border-radius:5px;background:var(--bg);padding:6px 7px">' + '<br>'.join(lines) + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

def txt(s, size="10px"):
    return '<span style="font-size:' + size + ';line-height:1.55">' + s + '</span>'

def mono(s, color="var(--fg-muted)"):
    return '<span style="font-family:var(--mono);font-size:9.5px;color:' + color + '">' + s + '</span>'
