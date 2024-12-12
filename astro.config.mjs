import { defineConfig } from 'astro/config';
import staticSite from '@astrojs/static-site';

export default defineConfig({
  base: '/sridharrg.github.io/', 
  output: 'static',
  adapter: staticSite(),
});

