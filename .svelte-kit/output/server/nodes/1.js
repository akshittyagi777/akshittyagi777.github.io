

export const index = 1;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/fallbacks/error.svelte.js')).default;
export const imports = ["_app/immutable/nodes/1.BH4ijwN8.js","_app/immutable/chunks/D-6aCaAD.js","_app/immutable/chunks/IHki7fMi.js","_app/immutable/chunks/CvayqYQG.js"];
export const stylesheets = [];
export const fonts = [];
