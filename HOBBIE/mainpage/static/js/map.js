function slotRenderCallback(e) {
    var t = $("#ads_ldr_top");
    if (e.slot.getAdUnitPath() === t.data("dfpslot")) {
        var o, n = $(" > div > iframe", t), i = !1;
        fixIframeHeight(n[0]), o = t.height(), $(n).on("mouseover mouseout", function (e) {
            i && clearTimeout(i), "mouseover" == e.type ? i = setTimeout(function () {
                fixIframeHeight(n[0])
            }, 100) : "mouseout" == e.type && (i = setTimeout(function () {
                fixIframeHeight(n[0], o)
            }, 100))
        })
    }
}
function fixIframeHeight(e, t) {
    var o = e.contentDocument ? e.contentDocument : e.contentWindow.document, n = o.body, i = o.documentElement;
    e.style.height = "90px", t = t || Math.max(n.scrollHeight, n.offsetHeight, i.clientHeight, i.scrollHeight, i.offsetHeight), e.style.height = t + "px"
}
$(function() {
    "use strict";
    var e, t, o = 658810, n = ($(".map").css("background-image") || "").match(/\?(\w+)/), i = n ? "?" + n.pop() : "", a = $(window), r = $("body"), s = $(".b-category-list"), l = $(".b-cities a"), f = $("#region_image"), c = $('<div class="map-tooltip"></div>'), u = ($("#map-area"), $("#map-svg")), g = [], d = !1, p = u.length, m = {handler: function() {
            t = $(u.get(0).contentDocument), g = t.find(".j-map-item"), g.on("mouseenter mouseleave", function(e) {
                var t = $(this), o = "region_" + t.data("region");
                d = "region" === t.data("type"), m.toggleHover(o, "mouseenter" === e.type)
            }).on("click", function() {
                var e = "region_" + $(this).data("region");
                l.filter(function() {
                    return this.id === e
                })[0].click()
            }), a.off("load.svgfix")
        },toggleHover: function(t, o) {
            var n, i = 0 | t.substr(7);
            return $("#" + t).toggleClass("hover", o).attr("data-state", o ? "hover" : ""), p ? (m.toggleMapTooltip(i, o), o || clearTimeout(e), n = g.filter(function() {
                return $(this).data("region") === i
            }), void (n.length && n.each(function() {
                $(this).attr("data-state", o ? "hover" : "")
            }))) : $(".i-city-point_" + t).toggleClass("hover", o)
        },toggleMapTooltip: function(o, n) {
            return n && d ? (c.html(g.filter(function() {
                return $(this).data("region") === o
            }).data("title")), p ? t.on("mousemove.maptooltip", function(e) {
                c.css({left: u.offset().left + e.pageX + 10,top: u.offset().top + e.pageY + 10})
            }) : r.on("mousemove.maptooltip", function(e) {
                c.css({left: e.pageX + 10,top: e.pageY + 10})
            }), d = !1, void (e = setTimeout(function() {
                c.show()
            }, 200))) : ((t || r).off(".maptooltip"), c.hide())
        },toggleRegion: function(e) {
            var t = ("n" === this.id[0] ? "regio" : "") + this.id, n = "mouseenter" === e.type, a = $(this).data("iscity");
            return d = !1, m.toggleHover(t, n), t === "region_" + o ? void $("#crimea-region-img").toggleClass("crimea-region-img-light", n) : !$("#n_" + t.substr(7)).length || a ? !1 : void f.css("background-image", "url(" + static_prefix + "/s/a/i/" + (n ? "map-regions/" + t + ".png" + i : "0.gif") + ")")
        }};
    p ? (u.get(0).addEventListener("load", m.handler), a.on("load.svgfix", m.handler)) : $("#region-map area, #region-map-crimea area, .i-city-point").on("mouseenter mouseleave", m.toggleRegion), l.on("mouseenter mouseleave", m.toggleRegion), c.appendTo(r), $(".b-category-list .switcher .pseudo-link").on("click", function() {
        s.toggleClass("open"), s.hasClass("open") || $("html, body").delay(300).animate({scrollTop: s.offset().top - 20}, 300)
    })
}), function (e) {
    "use strict";
    var t = {ldr_top: 0, ldr_mid: 0, ldr_low: 0, vr_top: 0, vr_low: 0}, o = {storage: "sessionStorage"}, n = function (o, n) {
        function i() {
            var o = e.extend(t, JSON.parse(("sessionStorage" === f.params.storage && "undefined" != typeof window.sessionStorage ? sessionStorage.getItem(h) : e.cookie(h)) || "{}"));
            o[f.params.code]++, "sessionStorage" === f.params.storage && "undefined" != typeof window.sessionStorage ? sessionStorage.setItem(h, JSON.stringify(o)) : e.cookie(h, JSON.stringify(o), {path: "/"})
        }

        function a(t) {
            var n, i = e.Deferred(), a = !1;
            switch (t) {
                case "viewport":
                    a = Boolean(o.filter(":in-viewport").length);
                    break;
                case "full":
                    n = o.find("iframe").first(), a = Boolean("none" !== o.css("display") && n.length && n.height())
            }
            return a && i.resolve() || i.reject(), i.promise()
        }

        function r() {
            c || (c = setTimeout(function () {
                a("viewport").done(function () {
                    f.$window.off(["scroll.dfp_views_counter", f.params.code].join("_")), l()
                }), clearTimeout(c), c = null
            }, d))
        }

        function s() {
            clearTimeout(c), c = null, f.$window.on(["scroll.dfp_views_counter", f.params.code].join("_"), r)
        }

        function l() {
            a("full").done(i).fail(function () {
                var e = 0;
                g && (g = !1, u = setInterval(function () {
                    a("full").done(function () {
                        a("viewport").done(i).fail(s), clearInterval(u), u = null
                    }).fail(function () {
                        ++e > m && (clearInterval(u), u = null)
                    })
                }, p))
            })
        }

        {
            var f = this, c = null, u = null, g = !0, d = 50, p = 300, m = 10, h = "dfp_views";
            !function () {
                f.$window = e(window), f.params = n, a("viewport").done(l).fail(s)
            }()
        }
    };
    n.prototype = {destroy: function () {
        this.$window.off(["scroll.dfp_views_counter", this.params.code].join("_"))
    }}, e.fn.dfpViewsCounter = function (i) {
        return this.each(function () {
            var a = e(this), r = a.data("DfpViewsCounter");
            r && "string" == typeof i ? "function" == typeof r[i] && r[i]() : (i = e.extend({code: a.data("banner-code")}, o), i.code in t && a.data("DfpViewsCounter", new n(a, i)))
        })
    }, e(function () {
        e(".dfp").dfpViewsCounter()
    })
}(jQuery);

$(window).load(function () {
    var svg = document.querySelector('object').getSVGDocument().documentElement;
    var paths = svg.getElementsByTagName("path");
    var i;
    for (i=0; i<paths.length;i++) {
        paths[i].addEventListener('click', showAlert )
    }

    function showAlert(e) {
        var title = this.getAttribute("data-title");
        var id = this.getAttribute("data-region");
        var a_now = document.getElementById("region_" + id);
        a_now.click();
    }
});
