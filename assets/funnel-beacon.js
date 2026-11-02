/* First-party conversion-intent beacon (SOAP Autopilot / thesoapbook.com).
 *
 * Same discipline as the CBC beacon: records only {venture, event, page-path}. It exists
 * because the Stripe telemetry could see a checkout SESSION but nothing could see whether
 * anyone ever clicked through to it - visits and intent were invisible.
 *
 * Privacy: no cookies, no identifiers, no IP, no third-party tracker. Counts only.
 */
(function () {
  var V = "soap";
  // Absolute: the marketing site is static (GitHub Pages) and has no /t route of its own;
  // the collector lives behind the SOAP tunnel at app.thesoapbook.com/t.
  var URL = "https://app.thesoapbook.com/t";

  function send(ev) {
    try {
      var body = JSON.stringify({ v: V, e: ev, p: location.pathname });
      if (navigator.sendBeacon) {
        navigator.sendBeacon(URL, new Blob([body], { type: "text/plain;charset=UTF-8" }));
      } else {
        fetch(URL, {
          method: "POST",
          body: body,
          headers: { "Content-Type": "application/json" },
          keepalive: true,
          mode: "cors"
        });
      }
    } catch (e) { /* never break the page for telemetry */ }
  }

  document.addEventListener("click", function (ev) {
    var el = ev.target;
    var a = el && el.closest ? el.closest("a") : null;
    if (!a) { return; }
    var h = a.getAttribute("href") || "";
    if (h.indexOf("checkout.stripe.com") > -1 || h.indexOf("buy.stripe.com") > -1) { send("checkout_click"); }
    else if (h.indexOf("mailto:") === 0) { send("email_click"); }
    else if (h.indexOf("tel:") === 0) { send("tel_click"); }
  }, true);

  window.addEventListener("load", function () { send("view"); });
})();