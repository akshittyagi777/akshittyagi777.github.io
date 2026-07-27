export const manifest = (() => {
function __memo(fn) {
	let value;
	return () => value ??= (value = fn());
}

return {
	appDir: "_app",
	appPath: "_app",
	assets: new Set([".DS_Store","files/cvLatest.pdf","files/pyg.css","files/styles.css","images/favicon.png","images/fp2.jpg"]),
	mimeTypes: {".pdf":"application/pdf",".css":"text/css",".png":"image/png",".jpg":"image/jpeg"},
	_: {
		client: {start:"_app/immutable/entry/start.SjADomzu.js",app:"_app/immutable/entry/app.BxncbR8g.js",imports:["_app/immutable/entry/start.SjADomzu.js","_app/immutable/chunks/CMJqZY2z.js","_app/immutable/chunks/Dn0n6aLH.js","_app/immutable/entry/app.BxncbR8g.js","_app/immutable/chunks/Dn0n6aLH.js","_app/immutable/chunks/IHki7fMi.js"],stylesheets:[],fonts:[],uses_env_dynamic_public:false},
		nodes: [
			__memo(() => import('./nodes/0.js')),
			__memo(() => import('./nodes/1.js'))
		],
		remotes: {
			
		},
		routes: [
			
		],
		prerendered_routes: new Set(["/"]),
		matchers: async () => {
			
			return {  };
		},
		server_assets: {}
	}
}
})();
