# -*- coding: utf-8 -*-
"""14부 카드에서 같이 쓰는 작은 조각들."""

def ba(bad, good, why="", w="152px"):
    """나쁜 문구 / 고친 문구 두 칸."""
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid color-mix(in srgb, var(--danger) 45%, transparent);border-radius:6px;'
            'background:var(--surface);padding:6px 7px;display:grid;gap:2px">'
            '<span style="font-size:8px;font-weight:700;color:var(--danger)">흔한 문구</span>'
            '<span style="font-size:9.5px;line-height:1.5">' + bad + '</span></div>'
            '<div style="border:1px solid color-mix(in srgb, var(--accent) 45%, transparent);border-radius:6px;'
            'background:var(--surface);padding:6px 7px;display:grid;gap:2px">'
            '<span style="font-size:8px;font-weight:700;color:var(--accent)">고친 문구</span>'
            '<span style="font-size:9.5px;line-height:1.5">' + good + '</span></div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + why + '</span>' if why else '')
            + '</div>')

def one(txt, tag="", ok=None, note="", w="152px"):
    """문구 한 칸."""
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + col + ';border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:3px">'
            + ('<span style="font-size:8px;font-weight:700;color:' + col + '">' + tag + '</span>' if tag else '')
            + '<span style="font-size:10px;line-height:1.55">' + txt + '</span></div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

def btn(label, primary=True, w="auto"):
    if primary:
        return ('<span style="display:inline-block;background:var(--accent);color:#fff;border-radius:4px;'
                'padding:3px 10px;font-size:9px">' + label + '</span>')
    return ('<span style="display:inline-block;border:1px solid var(--line);border-radius:4px;'
            'padding:3px 10px;font-size:9px">' + label + '</span>')
