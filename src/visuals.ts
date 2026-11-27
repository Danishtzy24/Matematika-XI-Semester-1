import { icon, CHAPTER_ICONS } from './art';
import type { LessonSection, TopicPlayer } from './types';
/* math-player v2 — Papan Pengerjaan: soal & diketahui permanen, baris kumulatif
   seperti tulisan guru di papan, panggung visual besar, default manual. */
const z2 = (n: number) => String(n).padStart(2, '0');
export function playerHTML(s: LessonSection, chapterId: number){
 const p = s.player as TopicPlayer | undefined;
 if (!p) return '';
 const n = p.rows.length;
 return `<div class="math-player" data-mp="${s.id}" data-step="-1" data-total="${n}" aria-label="Contoh langkah demi langkah ${s.number}">
 <div class="mp-top">
  <span class="mp-tag">${icon(CHAPTER_ICONS[chapterId-1]||'quiz')} CONTOH ${s.number}</span>
  <span class="mp-state">Menunggu dimulai — tekan Langkah berikutnya</span>
 </div>
 <div class="mp-progress" role="group" aria-label="Lompat ke langkah">
  <button type="button" class="mp-chip selected" data-mp-jump="-1" aria-pressed="true"><b>SOAL</b></button>
  ${p.rows.map((r,i)=>`<button type="button" class="mp-chip" data-mp-jump="${i}" aria-pressed="false"><b>${z2(i+1)}</b>${r.title}</button>`).join('')}
  <button type="button" class="mp-chip mp-chip-end" data-mp-jump="${n}" aria-pressed="false"><b>HASIL</b></button>
 </div>
 <div class="mp-grid">
  <aside class="mp-left">
   <div class="mp-given">
    <h5>Diketahui</h5>
    <p class="mp-q">${p.soal}</p>
    <ul class="mp-known">${p.given.map(g=>`<li><span class="mp-sym">${g.sym}</span><span class="mp-val">${g.val}</span></li>`).join('')}</ul>
    <p class="mp-goal">${icon('arrow')}<span>Dicari: <b>${p.goal}</b></span></p>
   </div>
   <div class="mp-manual-note">${icon('bulb')}<div><small>CARA PAKAI</small><p>Cocokkan setiap angka di kartu ini dengan warna pada rumus, lalu majukan langkah satu per satu — pelan-pelan.</p></div></div>
  </aside>
  <div class="mp-main">
   <div class="mp-stage">
    <div class="mp-stage-cap"><span>VISUAL LANGKAH</span><i class="mp-position">SOAL</i></div>
    <div class="mp-scene" tabindex="0" role="img" aria-label="Diagram langkah">${p.scene}</div>
   </div>
   <div class="mp-board-wrap">
    <div class="mp-board-head"><span>PAPAN PENGERJAAN</span><span class="mp-track" aria-hidden="true"><i></i></span></div>
    <div class="mp-board">
     <div class="mp-row mp-row-formula${p.fColored ? ' colored' : ''}"><span class="mp-row-label">RUMUS</span><div class="mp-math">${p.fRow}</div></div>
     <div class="mp-rows-now"></div>
     <div class="mp-row mp-row-finish" hidden><span class="mp-row-label">HASIL</span><div class="mp-math">${p.finish}</div><p class="mp-finish-plain">${p.finishPlain}</p></div>
    </div>
   </div>
   <div class="mp-narr">
    <span class="mp-kicker">MULAI</span>
    <div class="mp-narr-body">
     <h4 class="mp-title">Soal &amp; rumus yang dipakai</h4>
     <p class="mp-tip">Samakan data soal dengan simbol pada rumus, lalu tekan <b>Langkah berikutnya</b>.</p>
     <button type="button" class="mp-why-toggle" data-mp-why aria-expanded="false" hidden>${icon('bulb')} Mengapa langkah ini?</button>
     <p class="mp-why" hidden></p>
    </div>
   </div>
  </div>
 </div>
 <div class="mp-actions">
  <button type="button" class="mp-btn" data-mp-prev>${icon('arrow-up')} Sebelumnya</button>
  <button type="button" class="mp-btn primary" data-mp-next>Langkah berikutnya ${icon('arrow')}</button>
  <button type="button" class="mp-btn ghost" data-mp-reset>${icon('redo')} Ulangi</button>
  <button type="button" class="mp-btn ghost" data-mp-auto aria-pressed="false">${icon('play')} Putar otomatis</button>
 </div>
</div>`}
export const VISUALS: Record<string, never> = {};
export function visualHTML(s: LessonSection, chapterId: number){return playerHTML(s, chapterId)}
