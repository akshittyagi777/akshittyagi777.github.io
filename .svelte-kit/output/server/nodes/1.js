

export const index = 1;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/fallbacks/error.svelte.js')).default;
export const imports = ["_app/immutable/nodes/1.B7rqp1qm.js","_app/immutable/chunks/D-6aCaAD.js","_app/immutable/chunks/IHki7fMi.js","_app/immutable/chunks/C8UYPI0A.js"];
export const stylesheets = [];
export const fonts = [];
