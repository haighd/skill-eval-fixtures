export const logger = {
  info: (msg: string, ...args: unknown[]): void => {
    process.stderr.write(`${msg} ${args.map(String).join(" ")}\n`);
  },
};
