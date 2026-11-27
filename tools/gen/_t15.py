# -*- coding: utf-8 -*-
"""15부 카드에서 같이 쓰는 조각."""

def code(lines, w="152px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--fg-muted)")
    body = '<br>'.join(lines)
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="font-family:var(--mono);font-size:9px;color:' + col + ';line-height:1.7;'
            'border:1px solid var(--line);border-radius:5px;background:var(--bg);padding:6px 7px">' + body + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

def card(inner, w="152px", note="", ok=None):
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + col + ';border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:5px">'
            + inner + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')

def btn(label, primary=True):
    if primary:
        return ('<span style="display:inline-block;background:var(--accent);color:#fff;border-radius:4px;'
                'padding:3px 10px;font-size:9px">' + label + '</span>')
    return ('<span style="display:inline-block;border:1px solid var(--line);border-radius:4px;'
            'padding:3px 10px;font-size:9px">' + label + '</span>')

def blocks(real=False, w="152px", note="", ok=None):
    """와이어 ↔ 시안 미니 화면."""
    col = "var(--accent)" if ok else ("var(--danger)" if ok is False else "var(--line)")
    def blk(width, h=7):
        return ('<span style="display:block;height:' + str(h) + 'px;width:' + width +
                ';background:var(--ink-100);border-radius:2px"></span>')
    if real:
        body = ('<div style="display:flex;align-items:center"><span style="font-size:9px;font-weight:700">정산 목록</span>'
                '<span style="margin-left:auto">' + btn('내보내기') + '</span></div>'
                '<div style="display:grid;gap:3px">'
                '<div style="display:flex;gap:5px;align-items:center;border:1px solid var(--line);border-radius:4px;padding:4px 5px">'
                '<span style="width:12px;height:12px;border-radius:3px;background:var(--accent-soft)"></span>'
                '<span style="flex:1;font-size:8.5px">모란상회 신길역점<span style="display:block;font-size:7.5px;color:var(--fg-muted)">1,284,000원</span></span></div>'
                '</div>')
    else:
        body = ('<div style="display:flex;align-items:center">' + blk('44%', 9) +
                '<span style="margin-left:auto;background:var(--ink-100);border-radius:3px;padding:4px 14px"></span></div>'
                '<div style="display:grid;gap:3px">'
                '<div style="display:flex;gap:5px;align-items:center;border:1px solid var(--line);border-radius:4px;padding:4px 5px">'
                '<span style="width:12px;height:12px;border-radius:3px;background:var(--ink-100)"></span>'
                '<span style="flex:1;display:grid;gap:2px">' + blk('62%') + blk('36%', 5) + '</span></div>'
                '</div>')
    return ('              <div style="width:100%;max-width:' + w + ';display:grid;gap:5px">'
            '<div style="border:1px solid ' + col + ';border-radius:6px;background:var(--surface);padding:7px;display:grid;gap:5px">'
            + body + '</div>'
            + ('<span style="font-size:8.5px;color:var(--fg-muted)">' + note + '</span>' if note else '')
            + '</div>')
