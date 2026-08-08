export const manifest = (() => {
function __memo(fn) {
	let value;
	return () => value ??= (value = fn());
}

return {
	appDir: "_app",
	appPath: "_app",
	assets: new Set([".DS_Store","files/Akshit_cv.pdf","files/noisyCoqa.pdf","files/pyg.css","files/styles.css","images/favicon.png","images/fp2.jpg","images/profile.jpg"]),
	mimeTypes: {".pdf":"application/pdf",".css":"text/css",".png":"image/png",".jpg":"image/jpeg"},
	_: {
		client: {start:"_app/immutable/entry/start.DimVpbbm.js",app:"_app/immutable/entry/app.CjWP4WHH.js",imports:["_app/immutable/entry/start.DimVpbbm.js","_app/immutable/chunks/BlF8cEof.js","_app/immutable/chunks/D-6aCaAD.js","_app/immutable/entry/app.CjWP4WHH.js","_app/immutable/chunks/D-6aCaAD.js","_app/immutable/chunks/IHki7fMi.js"],stylesheets:[],fonts:[],uses_env_dynamic_public:false},
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
