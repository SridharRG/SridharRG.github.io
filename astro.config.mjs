import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import react from "@astrojs/react";
import mdx from "@astrojs/mdx";
import vercel from "@astrojs/vercel/serverless";

import sitemap from "@astrojs/sitemap";

// https://astro.build/config
export default defineConfig({
  site: "https://sridharrg.github.io/",
  integrations: [
    tailwind(),
    react(),
    mdx({
      syntaxHighlight: "shiki",
      optimize: true,
    }),
    sitemap({
      priority: 1,
      changefreq: "daily",
      lastmod: new Date(),
    }),
  ],
  devToolbar: {
    enabled: false,
  },
  image: {
    domains: ["res.cloudinary.com"],
  },
  output: "hybrid",
  adapter: vercel(),
});
