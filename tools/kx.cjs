const katex = require('/home/user/mtk-node/node_modules/katex');
let raw = '';
process.stdin.on('data', d => raw += d).on('end', () => {
  let texs = [];
  try { texs = JSON.parse(raw).texs || []; } catch (e) {}
  const out = texs.map(t => {
    try { return katex.renderToString(t, { displayMode: true, throwOnError: true, strict: false }); }
    catch (e) { return null; }
  });
  process.stdout.write(JSON.stringify({ out }));
});
