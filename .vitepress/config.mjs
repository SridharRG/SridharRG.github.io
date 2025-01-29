import { defineConfig } from "vitepress";
import { sidebar } from "./sidebar.js";
// https://vitepress.dev/reference/site-config
export default defineConfig({
  // base: '/til/',
  title: "Personal Wiki",
  description:
    "A second brain, a humble repository where I gather and preserve everything I learn—raw, unfiltered, and striving for clarity amidst the currents of thought",
  sitemap: {
    hostname: "https://wiki.kafkaa.xyz",
  },
  head: [
    [
      "link",
      { rel: "icon", type: "image/png", sizes: "32x32", href: "/favicon.ico" },
    ],
  ],
  themeConfig: {
    logo: "/favicon.ico",
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      // { text: 'Home', link: '/' },
      { text: "Blog", link: "https://kafkaa.xyz/blog/" },
    ],

    sidebar: sidebar,

    socialLinks: [
      { icon: "github", link: "https://github.com/0xkafkaa" },
      { icon: "x", link: "https://x.com/0xkafkaa" },
    ],
    search: {
      provider: "local",
    },
  },
  cleanUrls: true,
});
