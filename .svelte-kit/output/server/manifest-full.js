export const manifest = (() => {
function __memo(fn) {
	let value;
	return () => value ??= (value = fn());
}

return {
	appDir: "_app",
	appPath: "_app",
	assets: new Set(["files/cvLatest.pdf","files/pyg.css","files/styles.css","images/favicon.png","images/fp2.jpg"]),
	mimeTypes: {".pdf":"application/pdf",".css":"text/css",".png":"image/png",".jpg":"image/jpeg"},
	_: {
		client: {start:"_app/immutable/entry/start.CXn_zE0S.js",app:"_app/immutable/entry/app.zyV0b_qj.js",imports:["_app/immutable/entry/start.CXn_zE0S.js","_app/immutable/chunks/CvayqYQG.js","_app/immutable/chunks/D-6aCaAD.js","_app/immutable/entry/app.zyV0b_qj.js","_app/immutable/chunks/D-6aCaAD.js","_app/immutable/chunks/IHki7fMi.js"],stylesheets:[],fonts:[],uses_env_dynamic_public:false},
		nodes: [
			__memo(() => import('./nodes/0.js')),
			__memo(() => import('./nodes/1.js')),
			__memo(() => import('./nodes/2.js'))
		],
		remotes: {
			
		},
		routes: [
			{
				id: "/",
				pattern: /^\/$/,
				params: [],
				page: { layouts: [0,], errors: [1,], leaf: 2 },
				endpoint: null
			}
		],
		prerendered_routes: new Set([]),
		matchers: async () => {
			
			return {  };
		},
		server_assets: {}
	}
}
})();
