# Chapter 11: package.json and node_modules

Node 20.11.1 is active. The AI has confirmed it with `node --version`. Now it tries to start the frontend development server by running the project's dev script:

```
npm run dev
```

This comes back immediately:

```
> neighborhood-meals-frontend@0.1.0 dev
> vite

sh: vite: command not found
```

`vite` is listed in `frontend/package.json`. The project knows it needs vite. It says so explicitly. So why can't the shell find it?

Because listing something in `package.json` doesn't install it. The manifest and the installed packages are two different things. `frontend/node_modules/` — the directory where installed packages live — doesn't exist yet.

---

## The Manifest and the Shelf

`package.json` is the frontend's manifest. It declares what the project is, what scripts it can run, and what packages it depends on. Think of it as the packing list from Chapter 8 — the document that describes what belongs in the project's environment.

But a packing list doesn't pack itself. Reading it doesn't fill the box.

`node_modules/` is the shelf. It's the local directory where the actual package files live — the downloaded code for every dependency the project declared. When vite is in `node_modules/`, the shell can find it. When `node_modules/` doesn't exist, the shell can't find anything, regardless of what `package.json` says.

That's what happened here. `package.json` correctly declares vite as a dependency. But `npm install` — the step that reads the manifest and downloads everything into `node_modules/` — hasn't run yet. The shelf is empty. The error is accurate.

---

## What package.json Contains

Open `frontend/package.json` and you'll see something like this:

```json
{
  "name": "neighborhood-meals-frontend",
  "version": "0.1.0",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "vite": "^5.0.0",
    "@vitejs/plugin-react": "^4.2.0"
  },
  "engines": {
    "node": ">=20.11.0"
  }
}
```

Each section does something specific.

**`name` and `version`** identify this package. These fields matter if the package were published to the npm registry, but for a private frontend app, they're mostly just labels.

**`scripts`** is where the AI finds the commands it runs. When you ask the AI to start the dev server, it runs `npm run dev`. npm looks up `dev` in this section and runs `vite`. That's the whole mechanism — `npm run` is just a shorthand that looks up the command in `scripts` and executes it. The `sh: vite: command not found` error happened because npm found `dev: "vite"` in `scripts`, tried to run `vite`, and the shell couldn't locate the binary.

**`dependencies`** is the list of packages the app needs to run. React and React DOM live here. These packages are required for the built app to work in a browser.

**`devDependencies`** is the list of packages needed for development but not for the built app itself. Vite is here because it's a development server and build tool — users of the final app never encounter it. Separating dev and runtime dependencies keeps the production build smaller.

**`engines`** declares what runtime versions this project supports. This is where `"node": ">=20.11.0"` lives — the same constraint that caused the `EBADENGINE` error in Chapter 10. npm reads this field and enforces it during install.

---

## Why node_modules Isn't in Git

If you look at `frontend/.gitignore`, you'll find `node_modules` listed there. It's intentionally excluded from version control.

The reason is size and redundancy. `node_modules/` for a typical frontend project can contain thousands of files and tens of thousands of subdirectories. Committing all of that would bloat the repository enormously, slow down every clone and pull, and create noise in every diff.

The other reason is that the directory is fully reproducible. Everything in `node_modules/` can be recreated from `package.json` (and from `package-lock.json` for exact versions). If you clone the repository and run `npm install`, you get the same `node_modules/` that any other developer gets. It's generated output, not source.

This is the same logic behind excluding `backend/.venv` from Git. Virtual environments and `node_modules/` are both local, generated, and reconstructible. They belong on disk but not in the repository.

---

## What package-lock.json Is

When `npm install` runs, it creates or updates a file called `package-lock.json`. This file is in the repository — unlike `node_modules/`, it's checked in.

Here's the distinction between the two files:

`package.json` uses version ranges. `"vite": "^5.0.0"` means: any version of vite from 5.0.0 up to (but not including) 6.0.0 is acceptable. On the day `npm install` runs, npm picks the latest version that satisfies that range.

`package-lock.json` records the exact version npm actually chose. If npm picked vite 5.1.4 today, the lockfile says `"version": "5.1.4"`. Tomorrow, if vite 5.2.0 is released, the lockfile still says `5.1.4`. When the AI installs from a lockfile, it installs that exact version — not whatever is latest.

This is reproducibility. Every developer cloning the project and running `npm install` gets the same versions. The lockfile is what makes that possible.

When the lockfile exists, the AI uses `npm ci` (clean install) rather than `npm install` in some contexts. `npm ci` reads the lockfile and installs exactly what it records, without resolving ranges. For setting up an existing project, that's more reliable.

---

## What npm install Does

`npm install` is the step that connects the manifest to the shelf.

> **What the AI Does:**
> With Node 20.11.1 active, the AI runs:
>
> ```
> cd frontend
> npm install
> ```
>
> npm reads `package.json` and `package-lock.json`, then downloads every declared package into `frontend/node_modules/`. You'll see output like:
>
> ```
> added 312 packages, and audited 313 packages in 14s
>
> 102 packages are looking for funding
>   run `npm fund` for details
>
> found 0 vulnerabilities
> ```
>
> `added 312 packages` is the important line. That's `node_modules/` being created and filled.

> **Watch For:**
> After the install, `frontend/node_modules/` exists as a directory. The AI can confirm this by checking for vite specifically:
>
> ```
> ls frontend/node_modules/.bin/vite
> ```
>
> If that path exists, the binary is there. `npm run dev` will work.

---

## After the Install

With `node_modules/` populated, the dev script resolves.

```
npm run dev
```

Now produces:

```
> neighborhood-meals-frontend@0.1.0 dev
> vite

  VITE v5.1.4  ready in 312 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
```

The shell found `vite` because it's now in `frontend/node_modules/.bin/`. npm knows to look there when running scripts. The dev server started. In this project, the frontend is configured to serve on `localhost:3000`, so that's where the app appears.

This is the same shape as the Python resolution in Chapter 6. Once the packages were installed into the right place, the import error went away. Here, once `node_modules/` was created with the right contents, the command not found error went away. The pattern is the same: declare dependencies in the manifest, install them locally, use them.

---

## What You Own

The AI manages the install. You own not undoing it — and knowing what to do if it gets undone.

**If you delete `node_modules/` accidentally**, the fix is `npm install` from the `frontend/` directory. The AI can run that. The directory will be recreated from the lockfile. The install takes a minute or two.

**If `node_modules/` becomes corrupted or mismatched** — sometimes this happens after a Node version switch or a partial install — the fix is to delete the directory and reinstall clean. The AI handles this with `rm -rf node_modules && npm install`. This is one of the few cases where deleting the directory is intentional.

> **Don't Do This:** Do not manually edit the version numbers in `package.json` to try to resolve a conflict or update a package. Version constraints interact with each other — bumping vite's version might break a plugin that depends on the previous version. If a package needs to be updated, ask the AI to do it. It knows how to check compatibility and update the lockfile correctly.

> **Don't Do This:** Do not run `npm install <package-name>` to add a package without knowing what it adds. Running `npm install react-router-dom`, for example, adds an entry to `package.json` and updates `package-lock.json`. That's a project-level change that should go through the AI, not an ad hoc command. The AI will install what's needed when it's needed, and it will add it to the correct section (`dependencies` vs `devDependencies`).

The `package.json` is the source of truth for what the frontend needs. If that file is accurate, the AI can set up the environment on any machine. If it drifts — packages installed manually, versions edited by hand, entries deleted without reinstalling — the project becomes harder to reproduce.

> **Key Takeaway:** `package.json` declares what the frontend needs. `node_modules/` is the local copy of those packages. The gap between them is closed by `npm install`. Until that step runs, nothing declared in `package.json` exists locally.

---

The frontend is running — but some problems can't be fixed by installing the right packages or switching to the right version, because some problems live at the machine level, and that's where the next part begins.
