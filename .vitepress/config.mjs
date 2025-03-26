import { defineConfig } from "vitepress";
import { sidebar } from "./sidebar.js";
// https://vitepress.dev/reference/site-config
export default defineConfig({
  // base: '/til/',
  title: "SOTC's Hackathon Wiki",
  description:
    "A repo for pushing all the guidelines and other information for the hackathon and its related events to manage with participants",
  sitemap: {
    hostname: "https://sridharrg.github.io/",
  },
  head: [
    [
      "link",
      { rel: "icon", type: "image/png", sizes: "32x32", href: "/favicon.png" },
    ],
  ],
  themeConfig: {
    logo: "/favicon.png",
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      // { text: 'Home', link: '/' },
      { text: "Blog", link: "https://sotcpu.me/" },
    ],

    sidebar: sidebar,

    socialLinks: [
      { icon: "gitlab", link: "https://gitlab.com/sotc/" },
      { icon: "linkedin", link: "https://www.linkedin.com/company/social-and-open-technology-community/?viewAsMember=true" },
    ],
    search: {
      provider: "local",
    },
  },
  cleanUrls: true,
});
