!(function (e, n) {
    "object" == typeof exports && "object" == typeof module ? (module.exports = n()) : "function" == typeof define && define.amd ? define([], n) : "object" == typeof exports ? (exports.feather = n()) : (e.feather = n());
})("undefined" != typeof self ? self : this, function () {
    return (function (e) {
        function n(t) {
            if (i[t]) return i[t].exports;
            var l = (i[t] = { i: t, l: !1, exports: {} });
            return e[t].call(l.exports, l, l.exports, n), (l.l = !0), l.exports;
        }
        var i = {};
        return (
            (n.m = e),
            (n.c = i),
            (n.d = function (e, i, t) {
                n.o(e, i) || Object.defineProperty(e, i, { configurable: !1, enumerable: !0, get: t });
            }),
            (n.n = function (e) {
                var i =
                    e && e.__esModule
                        ? function () {
                              return e.default;
                          }
                        : function () {
                              return e;
                          };
                return n.d(i, "a", i), i;
            }),
            (n.o = function (e, n) {
                return Object.prototype.hasOwnProperty.call(e, n);
            }),
            (n.p = ""),
            n((n.s = 49))
        );
    })([
        function (e, n, i) {
            var t = i(36)("wks"),
                l = i(15),
                r = i(1).Symbol,
                o = "function" == typeof r;
            (e.exports = function (e) {
                return t[e] || (t[e] = (o && r[e]) || (o ? r : l)("Symbol." + e));
            }).store = t;
        },
        function (e, n) {
            var i = (e.exports = "undefined" != typeof window && window.Math == Math ? window : "undefined" != typeof self && self.Math == Math ? self : Function("return this")());
            "number" == typeof __g && (__g = i);
        },
        function (e, n) {
            e.exports = function (e) {
                return "object" == typeof e ? null !== e : "function" == typeof e;
            };
        },
        function (e, n, i) {
            var t = i(1),
                l = i(7),
                r = i(8),
                o = i(10),
                a = i(11),
                c = function (e, n, i) {
                    var y,
                        p,
                        h,
                        x,
                        s = e & c.F,
                        u = e & c.G,
                        f = e & c.S,
                        d = e & c.P,
                        v = e & c.B,
                        g = u ? t : f ? t[n] || (t[n] = {}) : (t[n] || {}).prototype,
                        m = u ? l : l[n] || (l[n] = {}),
                        w = m.prototype || (m.prototype = {});
                    u && (i = n);
                    for (y in i)
                        (p = !s && g && void 0 !== g[y]), (h = (p ? g : i)[y]), (x = v && p ? a(h, t) : d && "function" == typeof h ? a(Function.call, h) : h), g && o(g, y, h, e & c.U), m[y] != h && r(m, y, x), d && w[y] != h && (w[y] = h);
                };
            (t.core = l), (c.F = 1), (c.G = 2), (c.S = 4), (c.P = 8), (c.B = 16), (c.W = 32), (c.U = 64), (c.R = 128), (e.exports = c);
        },
        function (e, n, i) {
            var t = i(9),
                l = i(29),
                r = i(31),
                o = Object.defineProperty;
            n.f = i(5)
                ? Object.defineProperty
                : function (e, n, i) {
                      if ((t(e), (n = r(n, !0)), t(i), l))
                          try {
                              return o(e, n, i);
                          } catch (e) {}
                      if ("get" in i || "set" in i) throw TypeError("Accessors not supported!");
                      return "value" in i && (e[n] = i.value), e;
                  };
        },
        function (e, n, i) {
            e.exports = !i(12)(function () {
                return (
                    7 !=
                    Object.defineProperty({}, "a", {
                        get: function () {
                            return 7;
                        },
                    }).a
                );
            });
        },
        function (e, n) {
            var i = {}.hasOwnProperty;
            e.exports = function (e, n) {
                return i.call(e, n);
            };
        },
        function (e, n) {
            var i = (e.exports = { version: "2.5.3" });
            "number" == typeof __e && (__e = i);
        },
        function (e, n, i) {
            var t = i(4),
                l = i(14);
            e.exports = i(5)
                ? function (e, n, i) {
                      return t.f(e, n, l(1, i));
                  }
                : function (e, n, i) {
                      return (e[n] = i), e;
                  };
        },
        function (e, n, i) {
            var t = i(2);
            e.exports = function (e) {
                if (!t(e)) throw TypeError(e + " is not an object!");
                return e;
            };
        },
        function (e, n, i) {
            var t = i(1),
                l = i(8),
                r = i(6),
                o = i(15)("src"),
                a = Function.toString,
                c = ("" + a).split("toString");
            (i(7).inspectSource = function (e) {
                return a.call(e);
            }),
                (e.exports = function (e, n, i, a) {
                    var y = "function" == typeof i;
                    y && (r(i, "name") || l(i, "name", n)), e[n] !== i && (y && (r(i, o) || l(i, o, e[n] ? "" + e[n] : c.join(String(n)))), e === t ? (e[n] = i) : a ? (e[n] ? (e[n] = i) : l(e, n, i)) : (delete e[n], l(e, n, i)));
                })(Function.prototype, "toString", function () {
                    return ("function" == typeof this && this[o]) || a.call(this);
                });
        },
        function (e, n, i) {
            var t = i(32);
            e.exports = function (e, n, i) {
                if ((t(e), void 0 === n)) return e;
                switch (i) {
                    case 1:
                        return function (i) {
                            return e.call(n, i);
                        };
                    case 2:
                        return function (i, t) {
                            return e.call(n, i, t);
                        };
                    case 3:
                        return function (i, t, l) {
                            return e.call(n, i, t, l);
                        };
                }
                return function () {
                    return e.apply(n, arguments);
                };
            };
        },
        function (e, n) {
            e.exports = function (e) {
                try {
                    return !!e();
                } catch (e) {
                    return !0;
                }
            };
        },
        function (e, n) {
            e.exports = {};
        },
        function (e, n) {
            e.exports = function (e, n) {
                return { enumerable: !(1 & e), configurable: !(2 & e), writable: !(4 & e), value: n };
            };
        },
        function (e, n) {
            var i = 0,
                t = Math.random();
            e.exports = function (e) {
                return "Symbol(".concat(void 0 === e ? "" : e, ")_", (++i + t).toString(36));
            };
        },
        function (e, n, i) {
            var t = i(34),
                l = i(19);
            e.exports = function (e) {
                return t(l(e));
            };
        },
        function (e, n, i) {
            var t = i(11),
                l = i(38),
                r = i(39),
                o = i(9),
                a = i(22),
                c = i(40),
                y = {},
                p = {},
                n = (e.exports = function (e, n, i, h, x) {
                    var s,
                        u,
                        f,
                        d,
                        v = x
                            ? function () {
                                  return e;
                              }
                            : c(e),
                        g = t(i, h, n ? 2 : 1),
                        m = 0;
                    if ("function" != typeof v) throw TypeError(e + " is not iterable!");
                    if (r(v)) {
                        for (s = a(e.length); s > m; m++) if ((d = n ? g(o((u = e[m]))[0], u[1]) : g(e[m])) === y || d === p) return d;
                    } else for (f = v.call(e); !(u = f.next()).done; ) if ((d = l(f, g, u.value, n)) === y || d === p) return d;
                });
            (n.BREAK = y), (n.RETURN = p);
        },
        function (e, n) {
            var i = Math.ceil,
                t = Math.floor;
            e.exports = function (e) {
                return isNaN((e = +e)) ? 0 : (e > 0 ? t : i)(e);
            };
        },
        function (e, n) {
            e.exports = function (e) {
                if (void 0 == e) throw TypeError("Can't call method on  " + e);
                return e;
            };
        },
        function (e, n, i) {
            "use strict";
            var t = i(52),
                l = i(3),
                r = i(10),
                o = i(8),
                a = i(6),
                c = i(13),
                y = i(53),
                p = i(24),
                h = i(59),
                x = i(0)("iterator"),
                s = !([].keys && "next" in [].keys()),
                u = function () {
                    return this;
                };
            e.exports = function (e, n, i, f, d, v, g) {
                y(i, n, f);
                var m,
                    w,
                    M,
                    b = function (e) {
                        if (!s && e in z) return z[e];
                        switch (e) {
                            case "keys":
                            case "values":
                                return function () {
                                    return new i(this, e);
                                };
                        }
                        return function () {
                            return new i(this, e);
                        };
                    },
                    _ = n + " Iterator",
                    A = "values" == d,
                    k = !1,
                    z = e.prototype,
                    S = z[x] || z["@@iterator"] || (d && z[d]),
                    H = (!s && S) || b(d),
                    V = d ? (A ? b("entries") : H) : void 0,
                    O = "Array" == n ? z.entries || S : S;
                if (
                    (O && (M = h(O.call(new e()))) !== Object.prototype && M.next && (p(M, _, !0), t || a(M, x) || o(M, x, u)),
                    A &&
                        S &&
                        "values" !== S.name &&
                        ((k = !0),
                        (H = function () {
                            return S.call(this);
                        })),
                    (t && !g) || (!s && !k && z[x]) || o(z, x, H),
                    (c[n] = H),
                    (c[_] = u),
                    d)
                )
                    if (((m = { values: A ? H : b("values"), keys: v ? H : b("keys"), entries: V }), g)) for (w in m) w in z || r(z, w, m[w]);
                    else l(l.P + l.F * (s || k), n, m);
                return m;
            };
        },
        function (e, n, i) {
            var t = i(55),
                l = i(37);
            e.exports =
                Object.keys ||
                function (e) {
                    return t(e, l);
                };
        },
        function (e, n, i) {
            var t = i(18),
                l = Math.min;
            e.exports = function (e) {
                return e > 0 ? l(t(e), 9007199254740991) : 0;
            };
        },
        function (e, n, i) {
            var t = i(36)("keys"),
                l = i(15);
            e.exports = function (e) {
                return t[e] || (t[e] = l(e));
            };
        },
        function (e, n, i) {
            var t = i(4).f,
                l = i(6),
                r = i(0)("toStringTag");
            e.exports = function (e, n, i) {
                e && !l((e = i ? e : e.prototype), r) && t(e, r, { configurable: !0, value: n });
            };
        },
        function (e, n, i) {
            var t = i(19);
            e.exports = function (e) {
                return Object(t(e));
            };
        },
        function (e, n, i) {
            var t = i(35),
                l = i(0)("toStringTag"),
                r =
                    "Arguments" ==
                    t(
                        (function () {
                            return arguments;
                        })()
                    ),
                o = function (e, n) {
                    try {
                        return e[n];
                    } catch (e) {}
                };
            e.exports = function (e) {
                var n, i, a;
                return void 0 === e ? "Undefined" : null === e ? "Null" : "string" == typeof (i = o((n = Object(e)), l)) ? i : r ? t(n) : "Object" == (a = t(n)) && "function" == typeof n.callee ? "Arguments" : a;
            };
        },
        function (e, n, i) {
            "use strict";
            function t(e) {
                return e && e.__esModule ? e : { default: e };
            }
            Object.defineProperty(n, "__esModule", { value: !0 });
            var l = i(86),
                r = t(l),
                o = i(88),
                a = t(o),
                c = i(89),
                y = t(c);
            n.default = Object.keys(a.default)
                .map(function (e) {
                    return new r.default(e, a.default[e], y.default[e]);
                })
                .reduce(function (e, n) {
                    return (e[n.name] = n), e;
                }, {});
        },
        function (e, n, i) {
            "use strict";
            var t = i(51)(!0);
            i(20)(
                String,
                "String",
                function (e) {
                    (this._t = String(e)), (this._i = 0);
                },
                function () {
                    var e,
                        n = this._t,
                        i = this._i;
                    return i >= n.length ? { value: void 0, done: !0 } : ((e = t(n, i)), (this._i += e.length), { value: e, done: !1 });
                }
            );
        },
        function (e, n, i) {
            e.exports =
                !i(5) &&
                !i(12)(function () {
                    return (
                        7 !=
                        Object.defineProperty(i(30)("div"), "a", {
                            get: function () {
                                return 7;
                            },
                        }).a
                    );
                });
        },
        function (e, n, i) {
            var t = i(2),
                l = i(1).document,
                r = t(l) && t(l.createElement);
            e.exports = function (e) {
                return r ? l.createElement(e) : {};
            };
        },
        function (e, n, i) {
            var t = i(2);
            e.exports = function (e, n) {
                if (!t(e)) return e;
                var i, l;
                if (n && "function" == typeof (i = e.toString) && !t((l = i.call(e)))) return l;
                if ("function" == typeof (i = e.valueOf) && !t((l = i.call(e)))) return l;
                if (!n && "function" == typeof (i = e.toString) && !t((l = i.call(e)))) return l;
                throw TypeError("Can't convert object to primitive value");
            };
        },
        function (e, n) {
            e.exports = function (e) {
                if ("function" != typeof e) throw TypeError(e + " is not a function!");
                return e;
            };
        },
        function (e, n, i) {
            var t = i(9),
                l = i(54),
                r = i(37),
                o = i(23)("IE_PROTO"),
                a = function () {},
                c = function () {
                    var e,
                        n = i(30)("iframe"),
                        t = r.length;
                    for (n.style.display = "none", i(58).appendChild(n), n.src = "javascript:", e = n.contentWindow.document, e.open(), e.write("<script>document.F=Object</script>"), e.close(), c = e.F; t--; ) delete c.prototype[r[t]];
                    return c();
                };
            e.exports =
                Object.create ||
                function (e, n) {
                    var i;
                    return null !== e ? ((a.prototype = t(e)), (i = new a()), (a.prototype = null), (i[o] = e)) : (i = c()), void 0 === n ? i : l(i, n);
                };
        },
        function (e, n, i) {
            var t = i(35);
            e.exports = Object("z").propertyIsEnumerable(0)
                ? Object
                : function (e) {
                      return "String" == t(e) ? e.split("") : Object(e);
                  };
        },
        function (e, n) {
            var i = {}.toString;
            e.exports = function (e) {
                return i.call(e).slice(8, -1);
            };
        },
        function (e, n, i) {
            var t = i(1),
                l = t["__core-js_shared__"] || (t["__core-js_shared__"] = {});
            e.exports = function (e) {
                return l[e] || (l[e] = {});
            };
        },
        function (e, n) {
            e.exports = "constructor,hasOwnProperty,isPrototypeOf,propertyIsEnumerable,toLocaleString,toString,valueOf".split(",");
        },
        function (e, n, i) {
            var t = i(9);
            e.exports = function (e, n, i, l) {
                try {
                    return l ? n(t(i)[0], i[1]) : n(i);
                } catch (n) {
                    var r = e.return;
                    throw (void 0 !== r && t(r.call(e)), n);
                }
            };
        },
        function (e, n, i) {
            var t = i(13),
                l = i(0)("iterator"),
                r = Array.prototype;
            e.exports = function (e) {
                return void 0 !== e && (t.Array === e || r[l] === e);
            };
        },
        function (e, n, i) {
            var t = i(26),
                l = i(0)("iterator"),
                r = i(13);
            e.exports = i(7).getIteratorMethod = function (e) {
                if (void 0 != e) return e[l] || e["@@iterator"] || r[t(e)];
            };
        },
        function (e, n, i) {
            var t = i(0)("iterator"),
                l = !1;
            try {
                var r = [7][t]();
                (r.return = function () {
                    l = !0;
                }),
                    Array.from(r, function () {
                        throw 2;
                    });
            } catch (e) {}
            e.exports = function (e, n) {
                if (!n && !l) return !1;
                var i = !1;
                try {
                    var r = [7],
                        o = r[t]();
                    (o.next = function () {
                        return { done: (i = !0) };
                    }),
                        (r[t] = function () {
                            return o;
                        }),
                        e(r);
                } catch (e) {}
                return i;
            };
        },
        function (e, n) {
            n.f = {}.propertyIsEnumerable;
        },
        function (e, n) {
            e.exports = function (e, n) {
                return { value: n, done: !!e };
            };
        },
        function (e, n, i) {
            var t = i(10);
            e.exports = function (e, n, i) {
                for (var l in n) t(e, l, n[l], i);
                return e;
            };
        },
        function (e, n) {
            e.exports = function (e, n, i, t) {
                if (!(e instanceof n) || (void 0 !== t && t in e)) throw TypeError(i + ": incorrect invocation!");
                return e;
            };
        },
        function (e, n, i) {
            var t = i(15)("meta"),
                l = i(2),
                r = i(6),
                o = i(4).f,
                a = 0,
                c =
                    Object.isExtensible ||
                    function () {
                        return !0;
                    },
                y = !i(12)(function () {
                    return c(Object.preventExtensions({}));
                }),
                p = function (e) {
                    o(e, t, { value: { i: "O" + ++a, w: {} } });
                },
                h = function (e, n) {
                    if (!l(e)) return "symbol" == typeof e ? e : ("string" == typeof e ? "S" : "P") + e;
                    if (!r(e, t)) {
                        if (!c(e)) return "F";
                        if (!n) return "E";
                        p(e);
                    }
                    return e[t].i;
                },
                x = function (e, n) {
                    if (!r(e, t)) {
                        if (!c(e)) return !0;
                        if (!n) return !1;
                        p(e);
                    }
                    return e[t].w;
                },
                s = function (e) {
                    return y && u.NEED && c(e) && !r(e, t) && p(e), e;
                },
                u = (e.exports = { KEY: t, NEED: !1, fastKey: h, getWeak: x, onFreeze: s });
        },
        function (e, n, i) {
            var t = i(2);
            e.exports = function (e, n) {
                if (!t(e) || e._t !== n) throw TypeError("Incompatible receiver, " + n + " required!");
                return e;
            };
        },
        function (e, n, i) {
            var t, l; /*!
  Copyright (c) 2016 Jed Watson.
  Licensed under the MIT License (MIT), see
  http://jedwatson.github.io/classnames
*/
            !(function () {
                "use strict";
                var i = (function () {
                    function e() {}
                    function n(e, n) {
                        for (var i = n.length, t = 0; t < i; ++t) r(e, n[t]);
                    }
                    function i(e, n) {
                        e[n] = !0;
                    }
                    function t(e, n) {
                        for (var i in n) a.call(n, i) && (e[i] = !!n[i]);
                    }
                    function l(e, n) {
                        for (var i = n.split(c), t = i.length, l = 0; l < t; ++l) e[i[l]] = !0;
                    }
                    function r(e, r) {
                        if (r) {
                            var o = typeof r;
                            "string" === o ? l(e, r) : Array.isArray(r) ? n(e, r) : "object" === o ? t(e, r) : "number" === o && i(e, r);
                        }
                    }
                    function o() {
                        for (var i = arguments.length, t = Array(i), l = 0; l < i; l++) t[l] = arguments[l];
                        var r = new e();
                        n(r, t);
                        var o = [];
                        for (var a in r) r[a] && o.push(a);
                        return o.join(" ");
                    }
                    e.prototype = Object.create(null);
                    var a = {}.hasOwnProperty,
                        c = /\s+/;
                    return o;
                })();
                void 0 !== e && e.exports
                    ? (e.exports = i)
                    : ((t = []),
                      void 0 !==
                          (l = function () {
                              return i;
                          }.apply(n, t)) && (e.exports = l));
            })();
        },
        function (e, n, i) {
            i(50), i(62), i(66), (e.exports = i(85));
        },
        function (e, n, i) {
            i(28), i(60), (e.exports = i(7).Array.from);
        },
        function (e, n, i) {
            var t = i(18),
                l = i(19);
            e.exports = function (e) {
                return function (n, i) {
                    var r,
                        o,
                        a = String(l(n)),
                        c = t(i),
                        y = a.length;
                    return c < 0 || c >= y
                        ? e
                            ? ""
                            : void 0
                        : ((r = a.charCodeAt(c)), r < 55296 || r > 56319 || c + 1 === y || (o = a.charCodeAt(c + 1)) < 56320 || o > 57343 ? (e ? a.charAt(c) : r) : e ? a.slice(c, c + 2) : o - 56320 + ((r - 55296) << 10) + 65536);
                };
            };
        },
        function (e, n) {
            e.exports = !1;
        },
        function (e, n, i) {
            "use strict";
            var t = i(33),
                l = i(14),
                r = i(24),
                o = {};
            i(8)(o, i(0)("iterator"), function () {
                return this;
            }),
                (e.exports = function (e, n, i) {
                    (e.prototype = t(o, { next: l(1, i) })), r(e, n + " Iterator");
                });
        },
        function (e, n, i) {
            var t = i(4),
                l = i(9),
                r = i(21);
            e.exports = i(5)
                ? Object.defineProperties
                : function (e, n) {
                      l(e);
                      for (var i, o = r(n), a = o.length, c = 0; a > c; ) t.f(e, (i = o[c++]), n[i]);
                      return e;
                  };
        },
        function (e, n, i) {
            var t = i(6),
                l = i(16),
                r = i(56)(!1),
                o = i(23)("IE_PROTO");
            e.exports = function (e, n) {
                var i,
                    a = l(e),
                    c = 0,
                    y = [];
                for (i in a) i != o && t(a, i) && y.push(i);
                for (; n.length > c; ) t(a, (i = n[c++])) && (~r(y, i) || y.push(i));
                return y;
            };
        },
        function (e, n, i) {
            var t = i(16),
                l = i(22),
                r = i(57);
            e.exports = function (e) {
                return function (n, i, o) {
                    var a,
                        c = t(n),
                        y = l(c.length),
                        p = r(o, y);
                    if (e && i != i) {
                        for (; y > p; ) if ((a = c[p++]) != a) return !0;
                    } else for (; y > p; p++) if ((e || p in c) && c[p] === i) return e || p || 0;
                    return !e && -1;
                };
            };
        },
        function (e, n, i) {
            var t = i(18),
                l = Math.max,
                r = Math.min;
            e.exports = function (e, n) {
                return (e = t(e)), e < 0 ? l(e + n, 0) : r(e, n);
            };
        },
        function (e, n, i) {
            var t = i(1).document;
            e.exports = t && t.documentElement;
        },
        function (e, n, i) {
            var t = i(6),
                l = i(25),
                r = i(23)("IE_PROTO"),
                o = Object.prototype;
            e.exports =
                Object.getPrototypeOf ||
                function (e) {
                    return (e = l(e)), t(e, r) ? e[r] : "function" == typeof e.constructor && e instanceof e.constructor ? e.constructor.prototype : e instanceof Object ? o : null;
                };
        },
        function (e, n, i) {
            "use strict";
            var t = i(11),
                l = i(3),
                r = i(25),
                o = i(38),
                a = i(39),
                c = i(22),
                y = i(61),
                p = i(40);
            l(
                l.S +
                    l.F *
                        !i(41)(function (e) {
                            Array.from(e);
                        }),
                "Array",
                {
                    from: function (e) {
                        var n,
                            i,
                            l,
                            h,
                            x = r(e),
                            s = "function" == typeof this ? this : Array,
                            u = arguments.length,
                            f = u > 1 ? arguments[1] : void 0,
                            d = void 0 !== f,
                            v = 0,
                            g = p(x);
                        if ((d && (f = t(f, u > 2 ? arguments[2] : void 0, 2)), void 0 == g || (s == Array && a(g)))) for (n = c(x.length), i = new s(n); n > v; v++) y(i, v, d ? f(x[v], v) : x[v]);
                        else for (h = g.call(x), i = new s(); !(l = h.next()).done; v++) y(i, v, d ? o(h, f, [l.value, v], !0) : l.value);
                        return (i.length = v), i;
                    },
                }
            );
        },
        function (e, n, i) {
            "use strict";
            var t = i(4),
                l = i(14);
            e.exports = function (e, n, i) {
                n in e ? t.f(e, n, l(0, i)) : (e[n] = i);
            };
        },
        function (e, n, i) {
            i(63), (e.exports = i(7).Object.assign);
        },
        function (e, n, i) {
            var t = i(3);
            t(t.S + t.F, "Object", { assign: i(64) });
        },
        function (e, n, i) {
            "use strict";
            var t = i(21),
                l = i(65),
                r = i(42),
                o = i(25),
                a = i(34),
                c = Object.assign;
            e.exports =
                !c ||
                i(12)(function () {
                    var e = {},
                        n = {},
                        i = Symbol(),
                        t = "abcdefghijklmnopqrst";
                    return (
                        (e[i] = 7),
                        t.split("").forEach(function (e) {
                            n[e] = e;
                        }),
                        7 != c({}, e)[i] || Object.keys(c({}, n)).join("") != t
                    );
                })
                    ? function (e, n) {
                          for (var i = o(e), c = arguments.length, y = 1, p = l.f, h = r.f; c > y; )
                              for (var x, s = a(arguments[y++]), u = p ? t(s).concat(p(s)) : t(s), f = u.length, d = 0; f > d; ) h.call(s, (x = u[d++])) && (i[x] = s[x]);
                          return i;
                      }
                    : c;
        },
        function (e, n) {
            n.f = Object.getOwnPropertySymbols;
        },
        function (e, n, i) {
            i(67), i(28), i(68), i(71), i(78), i(81), i(83), (e.exports = i(7).Set);
        },
        function (e, n, i) {
            "use strict";
            var t = i(26),
                l = {};
            (l[i(0)("toStringTag")] = "z"),
                l + "" != "[object z]" &&
                    i(10)(
                        Object.prototype,
                        "toString",
                        function () {
                            return "[object " + t(this) + "]";
                        },
                        !0
                    );
        },
        function (e, n, i) {
            for (
                var t = i(69),
                    l = i(21),
                    r = i(10),
                    o = i(1),
                    a = i(8),
                    c = i(13),
                    y = i(0),
                    p = y("iterator"),
                    h = y("toStringTag"),
                    x = c.Array,
                    s = {
                        CSSRuleList: !0,
                        CSSStyleDeclaration: !1,
                        CSSValueList: !1,
                        ClientRectList: !1,
                        DOMRectList: !1,
                        DOMStringList: !1,
                        DOMTokenList: !0,
                        DataTransferItemList: !1,
                        FileList: !1,
                        HTMLAllCollection: !1,
                        HTMLCollection: !1,
                        HTMLFormElement: !1,
                        HTMLSelectElement: !1,
                        MediaList: !0,
                        MimeTypeArray: !1,
                        NamedNodeMap: !1,
                        NodeList: !0,
                        PaintRequestList: !1,
                        Plugin: !1,
                        PluginArray: !1,
                        SVGLengthList: !1,
                        SVGNumberList: !1,
                        SVGPathSegList: !1,
                        SVGPointList: !1,
                        SVGStringList: !1,
                        SVGTransformList: !1,
                        SourceBufferList: !1,
                        StyleSheetList: !0,
                        TextTrackCueList: !1,
                        TextTrackList: !1,
                        TouchList: !1,
                    },
                    u = l(s),
                    f = 0;
                f < u.length;
                f++
            ) {
                var d,
                    v = u[f],
                    g = s[v],
                    m = o[v],
                    w = m && m.prototype;
                if (w && (w[p] || a(w, p, x), w[h] || a(w, h, v), (c[v] = x), g)) for (d in t) w[d] || r(w, d, t[d], !0);
            }
        },
        function (e, n, i) {
            "use strict";
            var t = i(70),
                l = i(43),
                r = i(13),
                o = i(16);
            (e.exports = i(20)(
                Array,
                "Array",
                function (e, n) {
                    (this._t = o(e)), (this._i = 0), (this._k = n);
                },
                function () {
                    var e = this._t,
                        n = this._k,
                        i = this._i++;
                    return !e || i >= e.length ? ((this._t = void 0), l(1)) : "keys" == n ? l(0, i) : "values" == n ? l(0, e[i]) : l(0, [i, e[i]]);
                },
                "values"
            )),
                (r.Arguments = r.Array),
                t("keys"),
                t("values"),
                t("entries");
        },
        function (e, n, i) {
            var t = i(0)("unscopables"),
                l = Array.prototype;
            void 0 == l[t] && i(8)(l, t, {}),
                (e.exports = function (e) {
                    l[t][e] = !0;
                });
        },
        function (e, n, i) {
            "use strict";
            var t = i(72),
                l = i(47);
            e.exports = i(74)(
                "Set",
                function (e) {
                    return function () {
                        return e(this, arguments.length > 0 ? arguments[0] : void 0);
                    };
                },
                {
                    add: function (e) {
                        return t.def(l(this, "Set"), (e = 0 === e ? 0 : e), e);
                    },
                },
                t
            );
        },
        function (e, n, i) {
            "use strict";
            var t = i(4).f,
                l = i(33),
                r = i(44),
                o = i(11),
                a = i(45),
                c = i(17),
                y = i(20),
                p = i(43),
                h = i(73),
                x = i(5),
                s = i(46).fastKey,
                u = i(47),
                f = x ? "_s" : "size",
                d = function (e, n) {
                    var i,
                        t = s(n);
                    if ("F" !== t) return e._i[t];
                    for (i = e._f; i; i = i.n) if (i.k == n) return i;
                };
            e.exports = {
                getConstructor: function (e, n, i, y) {
                    var p = e(function (e, t) {
                        a(e, p, n, "_i"), (e._t = n), (e._i = l(null)), (e._f = void 0), (e._l = void 0), (e[f] = 0), void 0 != t && c(t, i, e[y], e);
                    });
                    return (
                        r(p.prototype, {
                            clear: function () {
                                for (var e = u(this, n), i = e._i, t = e._f; t; t = t.n) (t.r = !0), t.p && (t.p = t.p.n = void 0), delete i[t.i];
                                (e._f = e._l = void 0), (e[f] = 0);
                            },
                            delete: function (e) {
                                var i = u(this, n),
                                    t = d(i, e);
                                if (t) {
                                    var l = t.n,
                                        r = t.p;
                                    delete i._i[t.i], (t.r = !0), r && (r.n = l), l && (l.p = r), i._f == t && (i._f = l), i._l == t && (i._l = r), i[f]--;
                                }
                                return !!t;
                            },
                            forEach: function (e) {
                                u(this, n);
                                for (var i, t = o(e, arguments.length > 1 ? arguments[1] : void 0, 3); (i = i ? i.n : this._f); ) for (t(i.v, i.k, this); i && i.r; ) i = i.p;
                            },
                            has: function (e) {
                                return !!d(u(this, n), e);
                            },
                        }),
                        x &&
                            t(p.prototype, "size", {
                                get: function () {
                                    return u(this, n)[f];
                                },
                            }),
                        p
                    );
                },
                def: function (e, n, i) {
                    var t,
                        l,
                        r = d(e, n);
                    return r ? (r.v = i) : ((e._l = r = { i: (l = s(n, !0)), k: n, v: i, p: (t = e._l), n: void 0, r: !1 }), e._f || (e._f = r), t && (t.n = r), e[f]++, "F" !== l && (e._i[l] = r)), e;
                },
                getEntry: d,
                setStrong: function (e, n, i) {
                    y(
                        e,
                        n,
                        function (e, i) {
                            (this._t = u(e, n)), (this._k = i), (this._l = void 0);
                        },
                        function () {
                            for (var e = this, n = e._k, i = e._l; i && i.r; ) i = i.p;
                            return e._t && (e._l = i = i ? i.n : e._t._f) ? ("keys" == n ? p(0, i.k) : "values" == n ? p(0, i.v) : p(0, [i.k, i.v])) : ((e._t = void 0), p(1));
                        },
                        i ? "entries" : "values",
                        !i,
                        !0
                    ),
                        h(n);
                },
            };
        },
        function (e, n, i) {
            "use strict";
            var t = i(1),
                l = i(4),
                r = i(5),
                o = i(0)("species");
            e.exports = function (e) {
                var n = t[e];
                r &&
                    n &&
                    !n[o] &&
                    l.f(n, o, {
                        configurable: !0,
                        get: function () {
                            return this;
                        },
                    });
            };
        },
        function (e, n, i) {
            "use strict";
            var t = i(1),
                l = i(3),
                r = i(10),
                o = i(44),
                a = i(46),
                c = i(17),
                y = i(45),
                p = i(2),
                h = i(12),
                x = i(41),
                s = i(24),
                u = i(75);
            e.exports = function (e, n, i, f, d, v) {
                var g = t[e],
                    m = g,
                    w = d ? "set" : "add",
                    M = m && m.prototype,
                    b = {},
                    _ = function (e) {
                        var n = M[e];
                        r(
                            M,
                            e,
                            "delete" == e
                                ? function (e) {
                                      return !(v && !p(e)) && n.call(this, 0 === e ? 0 : e);
                                  }
                                : "has" == e
                                ? function (e) {
                                      return !(v && !p(e)) && n.call(this, 0 === e ? 0 : e);
                                  }
                                : "get" == e
                                ? function (e) {
                                      return v && !p(e) ? void 0 : n.call(this, 0 === e ? 0 : e);
                                  }
                                : "add" == e
                                ? function (e) {
                                      return n.call(this, 0 === e ? 0 : e), this;
                                  }
                                : function (e, i) {
                                      return n.call(this, 0 === e ? 0 : e, i), this;
                                  }
                        );
                    };
                if (
                    "function" == typeof m &&
                    (v ||
                        (M.forEach &&
                            !h(function () {
                                new m().entries().next();
                            })))
                ) {
                    var A = new m(),
                        k = A[w](v ? {} : -0, 1) != A,
                        z = h(function () {
                            A.has(1);
                        }),
                        S = x(function (e) {
                            new m(e);
                        }),
                        H =
                            !v &&
                            h(function () {
                                for (var e = new m(), n = 5; n--; ) e[w](n, n);
                                return !e.has(-0);
                            });
                    S ||
                        ((m = n(function (n, i) {
                            y(n, m, e);
                            var t = u(new g(), n, m);
                            return void 0 != i && c(i, d, t[w], t), t;
                        })),
                        (m.prototype = M),
                        (M.constructor = m)),
                        (z || H) && (_("delete"), _("has"), d && _("get")),
                        (H || k) && _(w),
                        v && M.clear && delete M.clear;
                } else (m = f.getConstructor(n, e, d, w)), o(m.prototype, i), (a.NEED = !0);
                return s(m, e), (b[e] = m), l(l.G + l.W + l.F * (m != g), b), v || f.setStrong(m, e, d), m;
            };
        },
        function (e, n, i) {
            var t = i(2),
                l = i(76).set;
            e.exports = function (e, n, i) {
                var r,
                    o = n.constructor;
                return o !== i && "function" == typeof o && (r = o.prototype) !== i.prototype && t(r) && l && l(e, r), e;
            };
        },
        function (e, n, i) {
            var t = i(2),
                l = i(9),
                r = function (e, n) {
                    if ((l(e), !t(n) && null !== n)) throw TypeError(n + ": can't set as prototype!");
                };
            e.exports = {
                set:
                    Object.setPrototypeOf ||
                    ("__proto__" in {}
                        ? (function (e, n, t) {
                              try {
                                  (t = i(11)(Function.call, i(77).f(Object.prototype, "__proto__").set, 2)), t(e, []), (n = !(e instanceof Array));
                              } catch (e) {
                                  n = !0;
                              }
                              return function (e, i) {
                                  return r(e, i), n ? (e.__proto__ = i) : t(e, i), e;
                              };
                          })({}, !1)
                        : void 0),
                check: r,
            };
        },
        function (e, n, i) {
            var t = i(42),
                l = i(14),
                r = i(16),
                o = i(31),
                a = i(6),
                c = i(29),
                y = Object.getOwnPropertyDescriptor;
            n.f = i(5)
                ? y
                : function (e, n) {
                      if (((e = r(e)), (n = o(n, !0)), c))
                          try {
                              return y(e, n);
                          } catch (e) {}
                      if (a(e, n)) return l(!t.f.call(e, n), e[n]);
                  };
        },
        function (e, n, i) {
            var t = i(3);
            t(t.P + t.R, "Set", { toJSON: i(79)("Set") });
        },
        function (e, n, i) {
            var t = i(26),
                l = i(80);
            e.exports = function (e) {
                return function () {
                    if (t(this) != e) throw TypeError(e + "#toJSON isn't generic");
                    return l(this);
                };
            };
        },
        function (e, n, i) {
            var t = i(17);
            e.exports = function (e, n) {
                var i = [];
                return t(e, !1, i.push, i, n), i;
            };
        },
        function (e, n, i) {
            i(82)("Set");
        },
        function (e, n, i) {
            "use strict";
            var t = i(3);
            e.exports = function (e) {
                t(t.S, e, {
                    of: function () {
                        for (var e = arguments.length, n = new Array(e); e--; ) n[e] = arguments[e];
                        return new this(n);
                    },
                });
            };
        },
        function (e, n, i) {
            i(84)("Set");
        },
        function (e, n, i) {
            "use strict";
            var t = i(3),
                l = i(32),
                r = i(11),
                o = i(17);
            e.exports = function (e) {
                t(t.S, e, {
                    from: function (e) {
                        var n,
                            i,
                            t,
                            a,
                            c = arguments[1];
                        return (
                            l(this),
                            (n = void 0 !== c),
                            n && l(c),
                            void 0 == e
                                ? new this()
                                : ((i = []),
                                  n
                                      ? ((t = 0),
                                        (a = r(c, arguments[2], 2)),
                                        o(e, !1, function (e) {
                                            i.push(a(e, t++));
                                        }))
                                      : o(e, !1, i.push, i),
                                  new this(i))
                        );
                    },
                });
            };
        },
        function (e, n, i) {
            "use strict";
            function t(e) {
                return e && e.__esModule ? e : { default: e };
            }
            var l = i(27),
                r = t(l),
                o = i(90),
                a = t(o),
                c = i(91),
                y = t(c);
            e.exports = { icons: r.default, toSvg: a.default, replace: y.default };
        },
        function (e, n, i) {
            "use strict";
            function t(e) {
                return e && e.__esModule ? e : { default: e };
            }
            function l(e, n) {
                if (!(e instanceof n)) throw new TypeError("Cannot call a class as a function");
            }
            function r(e) {
                return Object.keys(e)
                    .map(function (n) {
                        return n + '="' + e[n] + '"';
                    })
                    .join(" ");
            }
            Object.defineProperty(n, "__esModule", { value: !0 });
            var o =
                    Object.assign ||
                    function (e) {
                        for (var n = 1; n < arguments.length; n++) {
                            var i = arguments[n];
                            for (var t in i) Object.prototype.hasOwnProperty.call(i, t) && (e[t] = i[t]);
                        }
                        return e;
                    },
                a = (function () {
                    function e(e, n) {
                        for (var i = 0; i < n.length; i++) {
                            var t = n[i];
                            (t.enumerable = t.enumerable || !1), (t.configurable = !0), "value" in t && (t.writable = !0), Object.defineProperty(e, t.key, t);
                        }
                    }
                    return function (n, i, t) {
                        return i && e(n.prototype, i), t && e(n, t), n;
                    };
                })(),
                c = i(48),
                y = t(c),
                p = i(87),
                h = t(p),
                x = (function () {
                    function e(n, i) {
                        var t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : [];
                        l(this, e), (this.name = n), (this.contents = i), (this.tags = t), (this.attrs = o({}, h.default, { class: "feather feather-" + n }));
                    }
                    return (
                        a(e, [
                            {
                                key: "toSvg",
                                value: function () {
                                    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
                                    return "<svg " + r(o({}, this.attrs, e, { class: (0, y.default)(this.attrs.class, e.class) })) + ">" + this.contents + "</svg>";
                                },
                            },
                            {
                                key: "toString",
                                value: function () {
                                    return this.contents;
                                },
                            },
                        ]),
                        e
                    );
                })();
            n.default = x;
        },
        function (e, n) {
            e.exports = { xmlns: "http://www.w3.org/2000/svg", width: 24, height: 24, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", "stroke-width": 2, "stroke-linecap": "round", "stroke-linejoin": "round" };
        },
        function (e, n) {
            e.exports = {
                activity: '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>',
                airplay: '<path d="M5 17H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-1"></path><polygon points="12 15 17 21 7 21 12 15"></polygon>',
                "alert-circle": '<circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12" y2="16"></line>',
                "alert-octagon": '<polygon points="7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86 7.86 2"></polygon><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12" y2="16"></line>',
                "alert-triangle": '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12" y2="17"></line>',
                "align-center": '<line x1="18" y1="10" x2="6" y2="10"></line><line x1="21" y1="6" x2="3" y2="6"></line><line x1="21" y1="14" x2="3" y2="14"></line><line x1="18" y1="18" x2="6" y2="18"></line>',
                "align-justify": '<line x1="21" y1="10" x2="3" y2="10"></line><line x1="21" y1="6" x2="3" y2="6"></line><line x1="21" y1="14" x2="3" y2="14"></line><line x1="21" y1="18" x2="3" y2="18"></line>',
                "align-left": '<line x1="17" y1="10" x2="3" y2="10"></line><line x1="21" y1="6" x2="3" y2="6"></line><line x1="21" y1="14" x2="3" y2="14"></line><line x1="17" y1="18" x2="3" y2="18"></line>',
                "align-right": '<line x1="21" y1="10" x2="7" y2="10"></line><line x1="21" y1="6" x2="3" y2="6"></line><line x1="21" y1="14" x2="3" y2="14"></line><line x1="21" y1="18" x2="7" y2="18"></line>',
                anchor: '<circle cx="12" cy="5" r="3"></circle><line x1="12" y1="22" x2="12" y2="8"></line><path d="M5 12H2a10 10 0 0 0 20 0h-3"></path>',
                aperture:
                    '<circle cx="12" cy="12" r="10"></circle><line x1="14.31" y1="8" x2="20.05" y2="17.94"></line><line x1="9.69" y1="8" x2="21.17" y2="8"></line><line x1="7.38" y1="12" x2="13.12" y2="2.06"></line><line x1="9.69" y1="16" x2="3.95" y2="6.06"></line><line x1="14.31" y1="16" x2="2.83" y2="16"></line><line x1="16.62" y1="12" x2="10.88" y2="21.94"></line>',
                "arrow-down-circle": '<circle cx="12" cy="12" r="10"></circle><polyline points="8 12 12 16 16 12"></polyline><line x1="12" y1="8" x2="12" y2="16"></line>',
                "arrow-down-left": '<line x1="17" y1="7" x2="7" y2="17"></line><polyline points="17 17 7 17 7 7"></polyline>',
                "arrow-down-right": '<line x1="7" y1="7" x2="17" y2="17"></line><polyline points="17 7 17 17 7 17"></polyline>',
                "arrow-down": '<line x1="12" y1="5" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline>',
                "arrow-left-circle": '<circle cx="12" cy="12" r="10"></circle><polyline points="12 8 8 12 12 16"></polyline><line x1="16" y1="12" x2="8" y2="12"></line>',
                "arrow-left": '<line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline>',
                "arrow-right-circle": '<circle cx="12" cy="12" r="10"></circle><polyline points="12 16 16 12 12 8"></polyline><line x1="8" y1="12" x2="16" y2="12"></line>',
                "arrow-right": '<line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline>',
                "arrow-up-circle": '<circle cx="12" cy="12" r="10"></circle><polyline points="16 12 12 8 8 12"></polyline><line x1="12" y1="16" x2="12" y2="8"></line>',
                "arrow-up-left": '<line x1="17" y1="17" x2="7" y2="7"></line><polyline points="7 17 7 7 17 7"></polyline>',
                "arrow-up-right": '<line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline>',
                "arrow-up": '<line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline>',
                "at-sign": '<circle cx="12" cy="12" r="4"></circle><path d="M16 8v5a3 3 0 0 0 6 0v-1a10 10 0 1 0-3.92 7.94"></path>',
                award: '<circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline>',
                "bar-chart-2": '<line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line>',
                "bar-chart": '<line x1="12" y1="20" x2="12" y2="10"></line><line x1="18" y1="20" x2="18" y2="4"></line><line x1="6" y1="20" x2="6" y2="16"></line>',
                "battery-charging": '<path d="M5 18H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h3.19M15 6h2a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-3.19"></path><line x1="23" y1="13" x2="23" y2="11"></line><polyline points="11 6 7 12 13 12 9 18"></polyline>',
                battery: '<rect x="1" y="6" width="18" height="12" rx="2" ry="2"></rect><line x1="23" y1="13" x2="23" y2="11"></line>',
                "bell-off": '<path d="M8.56 2.9A7 7 0 0 1 19 9v4m-2 4H2a3 3 0 0 0 3-3V9a7 7 0 0 1 .78-3.22M13.73 21a2 2 0 0 1-3.46 0"></path><line x1="1" y1="1" x2="23" y2="23"></line>',
                bell: '<path d="M22 17H2a3 3 0 0 0 3-3V9a7 7 0 0 1 14 0v5a3 3 0 0 0 3 3zm-8.27 4a2 2 0 0 1-3.46 0"></path>',
                bluetooth: '<polyline points="6.5 6.5 17.5 17.5 12 23 12 1 17.5 6.5 6.5 17.5"></polyline>',
                bold: '<path d="M6 4h8a4 4 0 0 1 4 4 4 4 0 0 1-4 4H6z"></path><path d="M6 12h9a4 4 0 0 1 4 4 4 4 0 0 1-4 4H6z"></path>',
                "book-open": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>',
                book: '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>',
                bookmark: '<path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>',
                box:
                    '<path d="M12.89 1.45l8 4A2 2 0 0 1 22 7.24v9.53a2 2 0 0 1-1.11 1.79l-8 4a2 2 0 0 1-1.79 0l-8-4a2 2 0 0 1-1.1-1.8V7.24a2 2 0 0 1 1.11-1.79l8-4a2 2 0 0 1 1.78 0z"></path><polyline points="2.32 6.16 12 11 21.68 6.16"></polyline><line x1="12" y1="22.76" x2="12" y2="11"></line>',
                briefcase: '<rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>',
                calendar: '<rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line>',
                "camera-off": '<line x1="1" y1="1" x2="23" y2="23"></line><path d="M21 21H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h3m3-3h6l2 3h4a2 2 0 0 1 2 2v9.34m-7.72-2.06a4 4 0 1 1-5.56-5.56"></path>',
                camera: '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle>',
                cast: '<path d="M2 16.1A5 5 0 0 1 5.9 20M2 12.05A9 9 0 0 1 9.95 20M2 8V6a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-6"></path><line x1="2" y1="20" x2="2" y2="20"></line>',
                "check-circle": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline>',
                "check-square": '<polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path>',
                check: '<polyline points="20 6 9 17 4 12"></polyline>',
                "chevron-down": '<polyline points="6 9 12 15 18 9"></polyline>',
                "chevron-left": '<polyline points="15 18 9 12 15 6"></polyline>',
                "chevron-right": '<polyline points="9 18 15 12 9 6"></polyline>',
                "chevron-up": '<polyline points="18 15 12 9 6 15"></polyline>',
                "chevrons-down": '<polyline points="7 13 12 18 17 13"></polyline><polyline points="7 6 12 11 17 6"></polyline>',
                "chevrons-left": '<polyline points="11 17 6 12 11 7"></polyline><polyline points="18 17 13 12 18 7"></polyline>',
                "chevrons-right": '<polyline points="13 17 18 12 13 7"></polyline><polyline points="6 17 11 12 6 7"></polyline>',
                "chevrons-up": '<polyline points="17 11 12 6 7 11"></polyline><polyline points="17 18 12 13 7 18"></polyline>',
                chrome:
                    '<circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="4"></circle><line x1="21.17" y1="8" x2="12" y2="8"></line><line x1="3.95" y1="6.06" x2="8.54" y2="14"></line><line x1="10.88" y1="21.94" x2="15.46" y2="14"></line>',
                circle: '<circle cx="12" cy="12" r="10"></circle>',
                clipboard: '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>',
                clock: '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
                "cloud-drizzle":
                    '<line x1="8" y1="19" x2="8" y2="21"></line><line x1="8" y1="13" x2="8" y2="15"></line><line x1="16" y1="19" x2="16" y2="21"></line><line x1="16" y1="13" x2="16" y2="15"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="12" y1="15" x2="12" y2="17"></line><path d="M20 16.58A5 5 0 0 0 18 7h-1.26A8 8 0 1 0 4 15.25"></path>',
                "cloud-lightning": '<path d="M19 16.9A5 5 0 0 0 18 7h-1.26a8 8 0 1 0-11.62 9"></path><polyline points="13 11 9 17 15 17 11 23"></polyline>',
                "cloud-off": '<path d="M22.61 16.95A5 5 0 0 0 18 10h-1.26a8 8 0 0 0-7.05-6M5 5a8 8 0 0 0 4 15h9a5 5 0 0 0 1.7-.3"></path><line x1="1" y1="1" x2="23" y2="23"></line>',
                "cloud-rain": '<line x1="16" y1="13" x2="16" y2="21"></line><line x1="8" y1="13" x2="8" y2="21"></line><line x1="12" y1="15" x2="12" y2="23"></line><path d="M20 16.58A5 5 0 0 0 18 7h-1.26A8 8 0 1 0 4 15.25"></path>',
                "cloud-snow":
                    '<path d="M20 17.58A5 5 0 0 0 18 8h-1.26A8 8 0 1 0 4 16.25"></path><line x1="8" y1="16" x2="8" y2="16"></line><line x1="8" y1="20" x2="8" y2="20"></line><line x1="12" y1="18" x2="12" y2="18"></line><line x1="12" y1="22" x2="12" y2="22"></line><line x1="16" y1="16" x2="16" y2="16"></line><line x1="16" y1="20" x2="16" y2="20"></line>',
                cloud: '<path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path>',
                code: '<polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline>',
                codepen:
                    '<polygon points="12 2 22 8.5 22 15.5 12 22 2 15.5 2 8.5 12 2"></polygon><line x1="12" y1="22" x2="12" y2="15.5"></line><polyline points="22 8.5 12 15.5 2 8.5"></polyline><polyline points="2 15.5 12 8.5 22 15.5"></polyline><line x1="12" y1="2" x2="12" y2="8.5"></line>',
                command: '<path d="M18 3a3 3 0 0 0-3 3v12a3 3 0 0 0 3 3 3 3 0 0 0 3-3 3 3 0 0 0-3-3H6a3 3 0 0 0-3 3 3 3 0 0 0 3 3 3 3 0 0 0 3-3V6a3 3 0 0 0-3-3 3 3 0 0 0-3 3 3 3 0 0 0 3 3h12a3 3 0 0 0 3-3 3 3 0 0 0-3-3z"></path>',
                compass: '<circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon>',
                copy: '<rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>',
                "corner-down-left": '<polyline points="9 10 4 15 9 20"></polyline><path d="M20 4v7a4 4 0 0 1-4 4H4"></path>',
                "corner-down-right": '<polyline points="15 10 20 15 15 20"></polyline><path d="M4 4v7a4 4 0 0 0 4 4h12"></path>',
                "corner-left-down": '<polyline points="14 15 9 20 4 15"></polyline><path d="M20 4h-7a4 4 0 0 0-4 4v12"></path>',
                "corner-left-up": '<polyline points="14 9 9 4 4 9"></polyline><path d="M20 20h-7a4 4 0 0 1-4-4V4"></path>',
                "corner-right-down": '<polyline points="10 15 15 20 20 15"></polyline><path d="M4 4h7a4 4 0 0 1 4 4v12"></path>',
                "corner-right-up": '<polyline points="10 9 15 4 20 9"></polyline><path d="M4 20h7a4 4 0 0 0 4-4V4"></path>',
                "corner-up-left": '<polyline points="9 14 4 9 9 4"></polyline><path d="M20 20v-7a4 4 0 0 0-4-4H4"></path>',
                "corner-up-right": '<polyline points="15 14 20 9 15 4"></polyline><path d="M4 20v-7a4 4 0 0 1 4-4h12"></path>',
                cpu:
                    '<rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line>',
                "credit-card": '<rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line>',
                crop: '<path d="M6.13 1L6 16a2 2 0 0 0 2 2h15"></path><path d="M1 6.13L16 6a2 2 0 0 1 2 2v15"></path>',
                crosshair:
                    '<circle cx="12" cy="12" r="10"></circle><line x1="22" y1="12" x2="18" y2="12"></line><line x1="6" y1="12" x2="2" y2="12"></line><line x1="12" y1="6" x2="12" y2="2"></line><line x1="12" y1="22" x2="12" y2="18"></line>',
                database: '<ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>',
                delete: '<path d="M21 4H8l-7 8 7 8h13a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2z"></path><line x1="18" y1="9" x2="12" y2="15"></line><line x1="12" y1="9" x2="18" y2="15"></line>',
                disc: '<circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="3"></circle>',
                "dollar-sign": '<line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>',
                "download-cloud": '<polyline points="8 17 12 21 16 17"></polyline><line x1="12" y1="12" x2="12" y2="21"></line><path d="M20.88 18.09A5 5 0 0 0 18 9h-1.26A8 8 0 1 0 3 16.29"></path>',
                download: '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line>',
                droplet: '<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"></path>',
                "edit-2": '<polygon points="16 3 21 8 8 21 3 21 3 16 16 3"></polygon>',
                "edit-3": '<polygon points="14 2 18 6 7 17 3 17 3 13 14 2"></polygon><line x1="3" y1="22" x2="21" y2="22"></line>',
                edit: '<path d="M20 14.66V20a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h5.34"></path><polygon points="18 2 22 6 12 16 8 16 8 12 18 2"></polygon>',
                "external-link": '<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line>',
                "eye-off":
                    '<path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line>',
                eye: '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle>',
                facebook: '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>',
                "fast-forward": '<polygon points="13 19 22 12 13 5 13 19"></polygon><polygon points="2 19 11 12 2 5 2 19"></polygon>',
                feather: '<path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"></path><line x1="16" y1="8" x2="2" y2="22"></line><line x1="17" y1="15" x2="9" y2="15"></line>',
                "file-minus": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="9" y1="15" x2="15" y2="15"></line>',
                "file-plus":
                    '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line>',
                "file-text":
                    '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline>',
                file: '<path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"></path><polyline points="13 2 13 9 20 9"></polyline>',
                film:
                    '<rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect><line x1="7" y1="2" x2="7" y2="22"></line><line x1="17" y1="2" x2="17" y2="22"></line><line x1="2" y1="12" x2="22" y2="12"></line><line x1="2" y1="7" x2="7" y2="7"></line><line x1="2" y1="17" x2="7" y2="17"></line><line x1="17" y1="17" x2="22" y2="17"></line><line x1="17" y1="7" x2="22" y2="7"></line>',
                filter: '<polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon>',
                flag: '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"></path><line x1="4" y1="22" x2="4" y2="15"></line>',
                "folder-minus": '<path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path><line x1="9" y1="14" x2="15" y2="14"></line>',
                "folder-plus": '<path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path><line x1="12" y1="11" x2="12" y2="17"></line><line x1="9" y1="14" x2="15" y2="14"></line>',
                folder: '<path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>',
                "git-branch": '<line x1="6" y1="3" x2="6" y2="15"></line><circle cx="18" cy="6" r="3"></circle><circle cx="6" cy="18" r="3"></circle><path d="M18 9a9 9 0 0 1-9 9"></path>',
                "git-commit": '<circle cx="12" cy="12" r="4"></circle><line x1="1.05" y1="12" x2="7" y2="12"></line><line x1="17.01" y1="12" x2="22.96" y2="12"></line>',
                "git-merge": '<circle cx="18" cy="18" r="3"></circle><circle cx="6" cy="6" r="3"></circle><path d="M6 21V9a9 9 0 0 0 9 9"></path>',
                "git-pull-request": '<circle cx="18" cy="18" r="3"></circle><circle cx="6" cy="6" r="3"></circle><path d="M13 6h3a2 2 0 0 1 2 2v7"></path><line x1="6" y1="9" x2="6" y2="21"></line>',
                github:
                    '<path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>',
                gitlab:
                    '<path d="M22.65 14.39L12 22.13 1.35 14.39a.84.84 0 0 1-.3-.94l1.22-3.78 2.44-7.51A.42.42 0 0 1 4.82 2a.43.43 0 0 1 .58 0 .42.42 0 0 1 .11.18l2.44 7.49h8.1l2.44-7.51A.42.42 0 0 1 18.6 2a.43.43 0 0 1 .58 0 .42.42 0 0 1 .11.18l2.44 7.51L23 13.45a.84.84 0 0 1-.35.94z"></path>',
                globe: '<circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>',
                grid: '<rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect>',
                "hard-drive":
                    '<line x1="22" y1="12" x2="2" y2="12"></line><path d="M5.45 5.11L2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"></path><line x1="6" y1="16" x2="6" y2="16"></line><line x1="10" y1="16" x2="10" y2="16"></line>',
                hash: '<line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line>',
                headphones: '<path d="M3 18v-6a9 9 0 0 1 18 0v6"></path><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"></path>',
                heart: '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>',
                "help-circle": '<path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="17" x2="12" y2="17"></line>',
                home: '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline>',
                image: '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline>',
                inbox: '<polyline points="22 12 16 12 14 15 10 15 8 12 2 12"></polyline><path d="M5.45 5.11L2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"></path>',
                info: '<circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12" y2="8"></line>',
                instagram: '<rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.5" y2="6.5"></line>',
                italic: '<line x1="19" y1="4" x2="10" y2="4"></line><line x1="14" y1="20" x2="5" y2="20"></line><line x1="15" y1="4" x2="9" y2="20"></line>',
                layers: '<polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline>',
                layout: '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line>',
                "life-buoy":
                    '<circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="4"></circle><line x1="4.93" y1="4.93" x2="9.17" y2="9.17"></line><line x1="14.83" y1="14.83" x2="19.07" y2="19.07"></line><line x1="14.83" y1="9.17" x2="19.07" y2="4.93"></line><line x1="14.83" y1="9.17" x2="18.36" y2="5.64"></line><line x1="4.93" y1="19.07" x2="9.17" y2="14.83"></line>',
                "link-2": '<path d="M15 7h3a5 5 0 0 1 5 5 5 5 0 0 1-5 5h-3m-6 0H6a5 5 0 0 1-5-5 5 5 0 0 1 5-5h3"></path><line x1="8" y1="12" x2="16" y2="12"></line>',
                link: '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>',
                linkedin: '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle>',
                list:
                    '<line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3" y2="6"></line><line x1="3" y1="12" x2="3" y2="12"></line><line x1="3" y1="18" x2="3" y2="18"></line>',
                loader:
                    '<line x1="12" y1="2" x2="12" y2="6"></line><line x1="12" y1="18" x2="12" y2="22"></line><line x1="4.93" y1="4.93" x2="7.76" y2="7.76"></line><line x1="16.24" y1="16.24" x2="19.07" y2="19.07"></line><line x1="2" y1="12" x2="6" y2="12"></line><line x1="18" y1="12" x2="22" y2="12"></line><line x1="4.93" y1="19.07" x2="7.76" y2="16.24"></line><line x1="16.24" y1="7.76" x2="19.07" y2="4.93"></line>',
                lock: '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path>',
                "log-in": '<path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path><polyline points="10 17 15 12 10 7"></polyline><line x1="15" y1="12" x2="3" y2="12"></line>',
                "log-out": '<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line>',
                mail: '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline>',
                "map-pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle>',
                map: '<polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"></polygon><line x1="8" y1="2" x2="8" y2="18"></line><line x1="16" y1="6" x2="16" y2="22"></line>',
                "maximize-2": '<polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" y1="3" x2="14" y2="10"></line><line x1="3" y1="21" x2="10" y2="14"></line>',
                maximize: '<path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path>',
                menu: '<line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line>',
                "message-circle": '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path>',
                "message-square": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>',
                "mic-off":
                    '<line x1="1" y1="1" x2="23" y2="23"></line><path d="M9 9v3a3 3 0 0 0 5.12 2.12M15 9.34V4a3 3 0 0 0-5.94-.6"></path><path d="M17 16.95A7 7 0 0 1 5 12v-2m14 0v2a7 7 0 0 1-.11 1.23"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line>',
                mic: '<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line>',
                "minimize-2": '<polyline points="4 14 10 14 10 20"></polyline><polyline points="20 10 14 10 14 4"></polyline><line x1="14" y1="10" x2="21" y2="3"></line><line x1="3" y1="21" x2="10" y2="14"></line>',
                minimize: '<path d="M8 3v3a2 2 0 0 1-2 2H3m18 0h-3a2 2 0 0 1-2-2V3m0 18v-3a2 2 0 0 1 2-2h3M3 16h3a2 2 0 0 1 2 2v3"></path>',
                "minus-circle": '<circle cx="12" cy="12" r="10"></circle><line x1="8" y1="12" x2="16" y2="12"></line>',
                "minus-square": '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="8" y1="12" x2="16" y2="12"></line>',
                minus: '<line x1="5" y1="12" x2="19" y2="12"></line>',
                monitor: '<rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line>',
                moon: '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>',
                "more-horizontal": '<circle cx="12" cy="12" r="1"></circle><circle cx="19" cy="12" r="1"></circle><circle cx="5" cy="12" r="1"></circle>',
                "more-vertical": '<circle cx="12" cy="12" r="1"></circle><circle cx="12" cy="5" r="1"></circle><circle cx="12" cy="19" r="1"></circle>',
                move:
                    '<polyline points="5 9 2 12 5 15"></polyline><polyline points="9 5 12 2 15 5"></polyline><polyline points="15 19 12 22 9 19"></polyline><polyline points="19 9 22 12 19 15"></polyline><line x1="2" y1="12" x2="22" y2="12"></line><line x1="12" y1="2" x2="12" y2="22"></line>',
                music: '<path d="M9 17H5a2 2 0 0 0-2 2 2 2 0 0 0 2 2h2a2 2 0 0 0 2-2zm12-2h-4a2 2 0 0 0-2 2 2 2 0 0 0 2 2h2a2 2 0 0 0 2-2z"></path><polyline points="9 17 9 5 21 3 21 15"></polyline>',
                "navigation-2": '<polygon points="12 2 19 21 12 17 5 21 12 2"></polygon>',
                navigation: '<polygon points="3 11 22 2 13 21 11 13 3 11"></polygon>',
                octagon: '<polygon points="7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86 7.86 2"></polygon>',
                package:
                    '<path d="M12.89 1.45l8 4A2 2 0 0 1 22 7.24v9.53a2 2 0 0 1-1.11 1.79l-8 4a2 2 0 0 1-1.79 0l-8-4a2 2 0 0 1-1.1-1.8V7.24a2 2 0 0 1 1.11-1.79l8-4a2 2 0 0 1 1.78 0z"></path><polyline points="2.32 6.16 12 11 21.68 6.16"></polyline><line x1="12" y1="22.76" x2="12" y2="11"></line><line x1="7" y1="3.5" x2="17" y2="8.5"></line>',
                paperclip: '<path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"></path>',
                "pause-circle": '<circle cx="12" cy="12" r="10"></circle><line x1="10" y1="15" x2="10" y2="9"></line><line x1="14" y1="15" x2="14" y2="9"></line>',
                pause: '<rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect>',
                percent: '<line x1="19" y1="5" x2="5" y2="19"></line><circle cx="6.5" cy="6.5" r="2.5"></circle><circle cx="17.5" cy="17.5" r="2.5"></circle>',
                "phone-call":
                    '<path d="M15.05 5A5 5 0 0 1 19 8.95M15.05 1A9 9 0 0 1 23 8.94m-1 7.98v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>',
                "phone-forwarded":
                    '<polyline points="19 1 23 5 19 9"></polyline><line x1="15" y1="5" x2="23" y2="5"></line><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>',
                "phone-incoming":
                    '<polyline points="16 2 16 8 22 8"></polyline><line x1="23" y1="1" x2="16" y2="8"></line><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>',
                "phone-missed":
                    '<line x1="23" y1="1" x2="17" y2="7"></line><line x1="17" y1="1" x2="23" y2="7"></line><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>',
                "phone-off":
                    '<path d="M10.68 13.31a16 16 0 0 0 3.41 2.6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7 2 2 0 0 1 1.72 2v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.42 19.42 0 0 1-3.33-2.67m-2.67-3.34a19.79 19.79 0 0 1-3.07-8.63A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91"></path><line x1="23" y1="1" x2="1" y2="23"></line>',
                "phone-outgoing":
                    '<polyline points="23 7 23 1 17 1"></polyline><line x1="16" y1="8" x2="23" y2="1"></line><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>',
                phone:
                    '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>',
                "pie-chart": '<path d="M21.21 15.89A10 10 0 1 1 8 2.83"></path><path d="M22 12A10 10 0 0 0 12 2v10z"></path>',
                "play-circle": '<circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon>',
                play: '<polygon points="5 3 19 12 5 21 5 3"></polygon>',
                "plus-circle": '<circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line>',
                "plus-square": '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line>',
                plus: '<line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line>',
                pocket: '<path d="M4 3h16a2 2 0 0 1 2 2v6a10 10 0 0 1-10 10A10 10 0 0 1 2 11V5a2 2 0 0 1 2-2z"></path><polyline points="8 10 12 14 16 10"></polyline>',
                power: '<path d="M18.36 6.64a9 9 0 1 1-12.73 0"></path><line x1="12" y1="2" x2="12" y2="12"></line>',
                printer: '<polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect>',
                radio: '<circle cx="12" cy="12" r="2"></circle><path d="M16.24 7.76a6 6 0 0 1 0 8.49m-8.48-.01a6 6 0 0 1 0-8.49m11.31-2.82a10 10 0 0 1 0 14.14m-14.14 0a10 10 0 0 1 0-14.14"></path>',
                "refresh-ccw": '<polyline points="1 4 1 10 7 10"></polyline><polyline points="23 20 23 14 17 14"></polyline><path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"></path>',
                "refresh-cw": '<polyline points="23 4 23 10 17 10"></polyline><polyline points="1 20 1 14 7 14"></polyline><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>',
                repeat: '<polyline points="17 1 21 5 17 9"></polyline><path d="M3 11V9a4 4 0 0 1 4-4h14"></path><polyline points="7 23 3 19 7 15"></polyline><path d="M21 13v2a4 4 0 0 1-4 4H3"></path>',
                rewind: '<polygon points="11 19 2 12 11 5 11 19"></polygon><polygon points="22 19 13 12 22 5 22 19"></polygon>',
                "rotate-ccw": '<polyline points="1 4 1 10 7 10"></polyline><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"></path>',
                "rotate-cw": '<polyline points="23 4 23 10 17 10"></polyline><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"></path>',
                rss: '<path d="M4 11a9 9 0 0 1 9 9"></path><path d="M4 4a16 16 0 0 1 16 16"></path><circle cx="5" cy="19" r="1"></circle>',
                save: '<path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path><polyline points="17 21 17 13 7 13 7 21"></polyline><polyline points="7 3 7 8 15 8"></polyline>',
                scissors:
                    '<circle cx="6" cy="6" r="3"></circle><circle cx="6" cy="18" r="3"></circle><line x1="20" y1="4" x2="8.12" y2="15.88"></line><line x1="14.47" y1="14.48" x2="20" y2="20"></line><line x1="8.12" y1="8.12" x2="12" y2="12"></line>',
                search: '<circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>',
                send: '<line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>',
                server: '<rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect><line x1="6" y1="6" x2="6" y2="6"></line><line x1="6" y1="18" x2="6" y2="18"></line>',
                settings:
                    '<circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>',
                "share-2":
                    '<circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line>',
                share: '<path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"></path><polyline points="16 6 12 2 8 6"></polyline><line x1="12" y1="2" x2="12" y2="15"></line>',
                "shield-off": '<path d="M19.69 14a6.9 6.9 0 0 0 .31-2V5l-8-3-3.16 1.18"></path><path d="M4.73 4.73L4 5v7c0 6 8 10 8 10a20.29 20.29 0 0 0 5.62-4.38"></path><line x1="1" y1="1" x2="23" y2="23"></line>',
                shield: '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>',
                "shopping-bag": '<path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path>',
                "shopping-cart": '<circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>',
                shuffle:
                    '<polyline points="16 3 21 3 21 8"></polyline><line x1="4" y1="20" x2="21" y2="3"></line><polyline points="21 16 21 21 16 21"></polyline><line x1="15" y1="15" x2="21" y2="21"></line><line x1="4" y1="4" x2="9" y2="9"></line>',
                sidebar: '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line>',
                "skip-back": '<polygon points="19 20 9 12 19 4 19 20"></polygon><line x1="5" y1="19" x2="5" y2="5"></line>',
                "skip-forward": '<polygon points="5 4 15 12 5 20 5 4"></polygon><line x1="19" y1="5" x2="19" y2="19"></line>',
                slack:
                    '<path d="M22.08 9C19.81 1.41 16.54-.35 9 1.92S-.35 7.46 1.92 15 7.46 24.35 15 22.08 24.35 16.54 22.08 9z"></path><line x1="12.57" y1="5.99" x2="16.15" y2="16.39"></line><line x1="7.85" y1="7.61" x2="11.43" y2="18.01"></line><line x1="16.39" y1="7.85" x2="5.99" y2="11.43"></line><line x1="18.01" y1="12.57" x2="7.61" y2="16.15"></line>',
                slash: '<circle cx="12" cy="12" r="10"></circle><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"></line>',
                sliders:
                    '<line x1="4" y1="21" x2="4" y2="14"></line><line x1="4" y1="10" x2="4" y2="3"></line><line x1="12" y1="21" x2="12" y2="12"></line><line x1="12" y1="8" x2="12" y2="3"></line><line x1="20" y1="21" x2="20" y2="16"></line><line x1="20" y1="12" x2="20" y2="3"></line><line x1="1" y1="14" x2="7" y2="14"></line><line x1="9" y1="8" x2="15" y2="8"></line><line x1="17" y1="16" x2="23" y2="16"></line>',
                smartphone: '<rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12" y2="18"></line>',
                speaker: '<rect x="4" y="2" width="16" height="20" rx="2" ry="2"></rect><circle cx="12" cy="14" r="4"></circle><line x1="12" y1="6" x2="12" y2="6"></line>',
                square: '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>',
                star: '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>',
                "stop-circle": '<circle cx="12" cy="12" r="10"></circle><rect x="9" y="9" width="6" height="6"></rect>',
                sun:
                    '<circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>',
                sunrise:
                    '<path d="M17 18a5 5 0 0 0-10 0"></path><line x1="12" y1="2" x2="12" y2="9"></line><line x1="4.22" y1="10.22" x2="5.64" y2="11.64"></line><line x1="1" y1="18" x2="3" y2="18"></line><line x1="21" y1="18" x2="23" y2="18"></line><line x1="18.36" y1="11.64" x2="19.78" y2="10.22"></line><line x1="23" y1="22" x2="1" y2="22"></line><polyline points="8 6 12 2 16 6"></polyline>',
                sunset:
                    '<path d="M17 18a5 5 0 0 0-10 0"></path><line x1="12" y1="9" x2="12" y2="2"></line><line x1="4.22" y1="10.22" x2="5.64" y2="11.64"></line><line x1="1" y1="18" x2="3" y2="18"></line><line x1="21" y1="18" x2="23" y2="18"></line><line x1="18.36" y1="11.64" x2="19.78" y2="10.22"></line><line x1="23" y1="22" x2="1" y2="22"></line><polyline points="16 5 12 9 8 5"></polyline>',
                tablet: '<rect x="4" y="2" width="16" height="20" rx="2" ry="2" transform="rotate(180 12 12)"></rect><line x1="12" y1="18" x2="12" y2="18"></line>',
                tag: '<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7" y2="7"></line>',
                target: '<circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle>',
                terminal: '<polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line>',
                thermometer: '<path d="M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z"></path>',
                "thumbs-down": '<path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17"></path>',
                "thumbs-up": '<path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path>',
                "toggle-left": '<rect x="1" y="5" width="22" height="14" rx="7" ry="7"></rect><circle cx="8" cy="12" r="3"></circle>',
                "toggle-right": '<rect x="1" y="5" width="22" height="14" rx="7" ry="7"></rect><circle cx="16" cy="12" r="3"></circle>',
                "trash-2":
                    '<polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line>',
                trash: '<polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>',
                "trending-down": '<polyline points="23 18 13.5 8.5 8.5 13.5 1 6"></polyline><polyline points="17 18 23 18 23 12"></polyline>',
                "trending-up": '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline>',
                triangle: '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>',
                truck: '<rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle>',
                tv: '<rect x="2" y="7" width="20" height="15" rx="2" ry="2"></rect><polyline points="17 2 12 7 7 2"></polyline>',
                twitter: '<path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>',
                type: '<polyline points="4 7 4 4 20 4 20 7"></polyline><line x1="9" y1="20" x2="15" y2="20"></line><line x1="12" y1="4" x2="12" y2="20"></line>',
                umbrella: '<path d="M23 12a11.05 11.05 0 0 0-22 0zm-5 7a3 3 0 0 1-6 0v-7"></path>',
                underline: '<path d="M6 3v7a6 6 0 0 0 6 6 6 6 0 0 0 6-6V3"></path><line x1="4" y1="21" x2="20" y2="21"></line>',
                unlock: '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 9.9-1"></path>',
                "upload-cloud":
                    '<polyline points="16 16 12 12 8 16"></polyline><line x1="12" y1="12" x2="12" y2="21"></line><path d="M20.39 18.39A5 5 0 0 0 18 9h-1.26A8 8 0 1 0 3 16.3"></path><polyline points="16 16 12 12 8 16"></polyline>',
                upload: '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line>',
                "user-check": '<path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="8.5" cy="7" r="4"></circle><polyline points="17 11 19 13 23 9"></polyline>',
                "user-minus": '<path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="8.5" cy="7" r="4"></circle><line x1="23" y1="11" x2="17" y2="11"></line>',
                "user-plus": '<path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="8.5" cy="7" r="4"></circle><line x1="20" y1="8" x2="20" y2="14"></line><line x1="23" y1="11" x2="17" y2="11"></line>',
                "user-x": '<path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="8.5" cy="7" r="4"></circle><line x1="18" y1="8" x2="23" y2="13"></line><line x1="23" y1="8" x2="18" y2="13"></line>',
                user: '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle>',
                users: '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path>',
                "video-off": '<path d="M16 16v1a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h2m5.66 0H14a2 2 0 0 1 2 2v3.34l1 1L23 7v10"></path><line x1="1" y1="1" x2="23" y2="23"></line>',
                video: '<polygon points="23 7 16 12 23 17 23 7"></polygon><rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect>',
                voicemail: '<circle cx="5.5" cy="11.5" r="4.5"></circle><circle cx="18.5" cy="11.5" r="4.5"></circle><line x1="5.5" y1="16" x2="18.5" y2="16"></line>',
                "volume-1": '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>',
                "volume-2": '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>',
                "volume-x": '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line>',
                volume: '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>',
                watch:
                    '<circle cx="12" cy="12" r="7"></circle><polyline points="12 9 12 12 13.5 13.5"></polyline><path d="M16.51 17.35l-.35 3.83a2 2 0 0 1-2 1.82H9.83a2 2 0 0 1-2-1.82l-.35-3.83m.01-10.7l.35-3.83A2 2 0 0 1 9.83 1h4.35a2 2 0 0 1 2 1.82l.35 3.83"></path>',
                "wifi-off":
                    '<line x1="1" y1="1" x2="23" y2="23"></line><path d="M16.72 11.06A10.94 10.94 0 0 1 19 12.55"></path><path d="M5 12.55a10.94 10.94 0 0 1 5.17-2.39"></path><path d="M10.71 5.05A16 16 0 0 1 22.58 9"></path><path d="M1.42 9a15.91 15.91 0 0 1 4.7-2.88"></path><path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path><line x1="12" y1="20" x2="12" y2="20"></line>',
                wifi: '<path d="M5 12.55a11 11 0 0 1 14.08 0"></path><path d="M1.42 9a16 16 0 0 1 21.16 0"></path><path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path><line x1="12" y1="20" x2="12" y2="20"></line>',
                wind: '<path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2"></path>',
                "x-circle": '<circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line>',
                "x-square": '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="9" x2="15" y2="15"></line><line x1="15" y1="9" x2="9" y2="15"></line>',
                x: '<line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line>',
                "zap-off":
                    '<polyline points="12.41 6.75 13 2 10.57 4.92"></polyline><polyline points="18.57 12.91 21 10 15.66 10"></polyline><polyline points="8 8 3 14 12 14 11 22 16 16"></polyline><line x1="1" y1="1" x2="23" y2="23"></line>',
                zap: '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>',
                "zoom-in": '<circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line>',
                "zoom-out": '<circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="8" y1="11" x2="14" y2="11"></line>',
            };
        },
        function (e, n) {
            e.exports = {
                activity: ["pulse", "health", "action", "motion"],
                airplay: ["stream", "cast", "mirroring"],
                "alert-circle": ["warning"],
                "alert-octagon": ["warning"],
                "alert-triangle": ["warning"],
                "at-sign": ["mention"],
                award: ["achievement", "badge"],
                aperture: ["camera", "photo"],
                bell: ["alarm", "notification"],
                "bell-off": ["alarm", "notification", "silent"],
                bluetooth: ["wireless"],
                "book-open": ["read"],
                book: ["read", "dictionary", "booklet", "magazine"],
                bookmark: ["read", "clip", "marker", "tag"],
                briefcase: ["work", "bag", "baggage", "folder"],
                clipboard: ["copy"],
                clock: ["time", "watch", "alarm"],
                "cloud-drizzle": ["weather", "shower"],
                "cloud-lightning": ["weather", "bolt"],
                "cloud-rain": ["weather"],
                "cloud-snow": ["weather", "blizzard"],
                cloud: ["weather"],
                codepen: ["logo"],
                command: ["keyboard", "cmd"],
                compass: ["navigation", "safari", "travel"],
                copy: ["clone", "duplicate"],
                "corner-down-left": ["arrow"],
                "corner-down-right": ["arrow"],
                "corner-left-down": ["arrow"],
                "corner-left-up": ["arrow"],
                "corner-right-down": ["arrow"],
                "corner-right-up": ["arrow"],
                "corner-up-left": ["arrow"],
                "corner-up-right": ["arrow"],
                "credit-card": ["purchase", "payment", "cc"],
                crop: ["photo", "image"],
                crosshair: ["aim", "target"],
                database: ["storage"],
                delete: ["remove"],
                disc: ["album", "cd", "dvd", "music"],
                "dollar-sign": ["currency", "money", "payment"],
                droplet: ["water"],
                edit: ["pencil", "change"],
                "edit-2": ["pencil", "change"],
                "edit-3": ["pencil", "change"],
                eye: ["view", "watch"],
                "eye-off": ["view", "watch"],
                "external-link": ["outbound"],
                facebook: ["logo"],
                "fast-forward": ["music"],
                film: ["movie", "video"],
                "folder-minus": ["directory"],
                "folder-plus": ["directory"],
                folder: ["directory"],
                "git-branch": ["code", "version control"],
                "git-commit": ["code", "version control"],
                "git-merge": ["code", "version control"],
                "git-pull-request": ["code", "version control"],
                github: ["logo", "version control"],
                gitlab: ["logo", "version control"],
                global: ["world", "browser", "language", "translate"],
                "hard-drive": ["computer", "server"],
                hash: ["hashtag", "number", "pound"],
                headphones: ["music", "audio"],
                heart: ["like", "love"],
                "help-circle": ["question mark"],
                home: ["house"],
                image: ["picture"],
                inbox: ["email"],
                instagram: ["logo", "camera"],
                "life-bouy": ["help", "life ring", "support"],
                linkedin: ["logo"],
                lock: ["security", "password"],
                "log-in": ["sign in", "arrow"],
                "log-out": ["sign out", "arrow"],
                mail: ["email"],
                "map-pin": ["location", "navigation", "travel", "marker"],
                map: ["location", "navigation", "travel"],
                maximize: ["fullscreen"],
                "maximize-2": ["fullscreen", "arrows"],
                menu: ["bars", "navigation", "hamburger"],
                "message-circle": ["comment", "chat"],
                "message-square": ["comment", "chat"],
                "mic-off": ["record"],
                mic: ["record"],
                minimize: ["exit fullscreen"],
                "minimize-2": ["exit fullscreen", "arrows"],
                monitor: ["tv"],
                moon: ["dark", "night"],
                "more-horizontal": ["ellipsis"],
                "more-vertical": ["ellipsis"],
                move: ["arrows"],
                navigation: ["location", "travel"],
                "navigation-2": ["location", "travel"],
                octagon: ["stop"],
                package: ["box"],
                paperclip: ["attachment"],
                pause: ["music", "stop"],
                "pause-circle": ["music", "stop"],
                play: ["music", "start"],
                "play-circle": ["music", "start"],
                plus: ["add", "new"],
                "plus-circle": ["add", "new"],
                "plus-square": ["add", "new"],
                pocket: ["logo", "save"],
                power: ["on", "off"],
                radio: ["signal"],
                rewind: ["music"],
                rss: ["feed", "subscribe"],
                save: ["floppy disk"],
                send: ["message", "mail", "paper airplane"],
                settings: ["cog", "edit", "gear", "preferences"],
                shield: ["security"],
                "shield-off": ["security"],
                "shopping-bag": ["ecommerce", "cart", "purchase", "store"],
                "shopping-cart": ["ecommerce", "cart", "purchase", "store"],
                shuffle: ["music"],
                "skip-back": ["music"],
                "skip-forward": ["music"],
                slash: ["ban", "no"],
                sliders: ["settings", "controls"],
                speaker: ["music"],
                star: ["bookmark", "favorite", "like"],
                sun: ["brightness", "weather", "light"],
                sunrise: ["weather"],
                sunset: ["weather"],
                tag: ["label"],
                target: ["bullseye"],
                terminal: ["code", "command line"],
                "thumbs-down": ["dislike", "bad"],
                "thumbs-up": ["like", "good"],
                "toggle-left": ["on", "off", "switch"],
                "toggle-right": ["on", "off", "switch"],
                trash: ["garbage", "delete", "remove"],
                "trash-2": ["garbage", "delete", "remove"],
                triangle: ["delta"],
                truck: ["delivery", "van", "shipping"],
                twitter: ["logo"],
                umbrella: ["rain", "weather"],
                "video-off": ["camera", "movie", "film"],
                video: ["camera", "movie", "film"],
                voicemail: ["phone"],
                volume: ["music", "sound", "mute"],
                "volume-1": ["music", "sound"],
                "volume-2": ["music", "sound"],
                "volume-x": ["music", "sound", "mute"],
                watch: ["clock", "time"],
                wind: ["weather", "air"],
                "x-circle": ["cancel", "close", "delete", "remove", "times"],
                "x-square": ["cancel", "close", "delete", "remove", "times"],
                x: ["cancel", "close", "delete", "remove", "times"],
                "zap-off": ["flash", "camera", "lightning"],
                zap: ["flash", "camera", "lightning"],
            };
        },
        function (e, n, i) {
            "use strict";
            function t(e) {
                var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {};
                if ((console.warn("feather.toSvg() is deprecated. Please use feather.icons[name].toSvg() instead."), !e)) throw new Error("The required `key` (icon name) parameter is missing.");
                if (!r.default[e]) throw new Error("No icon matching '" + e + "'. See the complete list of icons at https://feathericons.com");
                return r.default[e].toSvg(n);
            }
            Object.defineProperty(n, "__esModule", { value: !0 });
            var l = i(27),
                r = (function (e) {
                    return e && e.__esModule ? e : { default: e };
                })(l);
            n.default = t;
        },
        function (e, n, i) {
            "use strict";
            function t(e) {
                return e && e.__esModule ? e : { default: e };
            }
            function l() {
                var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
                if ("undefined" == typeof document) throw new Error("`feather.replace()` only works in a browser environment.");
                var n = document.querySelectorAll("[data-feather]");
                Array.from(n).forEach(function (n) {
                    return r(n, e);
                });
            }
            function r(e) {
                var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {},
                    i = o(e),
                    t = i["data-feather"];
                delete i["data-feather"];
                var l = h.default[t].toSvg(a({}, n, i, { class: (0, y.default)(n.class, i.class) })),
                    r = new DOMParser().parseFromString(l, "image/svg+xml"),
                    c = r.querySelector("svg");
                e.parentNode.replaceChild(c, e);
            }
            function o(e) {
                return Array.from(e.attributes).reduce(function (e, n) {
                    return (e[n.name] = n.value), e;
                }, {});
            }
            Object.defineProperty(n, "__esModule", { value: !0 });
            var a =
                    Object.assign ||
                    function (e) {
                        for (var n = 1; n < arguments.length; n++) {
                            var i = arguments[n];
                            for (var t in i) Object.prototype.hasOwnProperty.call(i, t) && (e[t] = i[t]);
                        }
                        return e;
                    },
                c = i(48),
                y = t(c),
                p = i(27),
                h = t(p);
            n.default = l;
        },
    ]);
});
//# sourceMappingURL=feather.min.js.map
