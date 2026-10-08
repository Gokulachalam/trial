  window.__miqStep2Shown = function (kbName, kbDesc) {
    mqKb = { name: kbName || '', description: kbDesc || '' };
    if (!MQ) MQ = mqFresh();
    mqRender();
  };
  window.__miqValidate = mqValidate;
  window.__migrateiqSnapshot = mqSnapshot;
  window.__miqReset = function () { MQ = mqFresh(); mqError(null); mqRender(); };
  window.__miqDrawerHtml = mqDrawerHtml;

  initLookupLibrary();
  initPipelines();
  MQ = mqFresh();
})();
</script>

</body>