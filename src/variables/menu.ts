export type TMenu = {
  text: string;
  href: string;
  title: string;
  external?: boolean;
};

export let menu: Array<TMenu> = [
  { text: "Home", href: "/", title: "Homepage" },
  { text: "guidelines", href: "https://gitlab.com/sotc/hackathon/-/raw/main/guidelines/sotc-hackathon-guidelines.pdf?ref_type=heads&inline=false", title: "guidelines" },
  {
    text: "LInkedIn",
    href: "https://www.linkedin.com/company/social-and-open-technology-community/",
    title: "Linkedin",
    external: true,
  },
  {
    text: "gitlab",
    href: "https://gitlab.com/sotc",
    title: "Gitlab",
    external: true,
  },
];
